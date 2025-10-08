from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import OrderForm
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .models import Order, OrderLineItem
from books.models import Books
from bag.contexts import bag_contents
from bag.utils import get_or_create_cart

import stripe
import json

def send_confirmation_email(order):
    """
    Send order confirmation email immediately
    """
    try:
        print(f"Attempting to send email to: {order.email}")  # Debug print
        
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        ).strip()  # Remove any trailing newlines
        
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        
        print(f"Email subject: {subject}")  # Debug print
        print(f"Sending from: {settings.DEFAULT_FROM_EMAIL}")  # Debug print
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            fail_silently=False,  # This will raise exceptions if email fails
        )
        
        order.email_sent = True
        order.save()
        print(f"Email successfully sent to {order.email}")  # Debug print
        return True
    except Exception as e:
        print(f"Error sending confirmation email for order {order.order_number}: {e}")
        print(f"Error type: {type(e).__name__}")  # Show error type
        return False

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        # Get cart items for metadata
        cart = get_or_create_cart(request)
        cart_data = {}
        for item in cart.items.all():
            if item.book.isbn not in cart_data:
                cart_data[item.book.isbn] = {}
            cart_data[item.book.isbn][item.format] = item.quantity
        
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(cart_data),
            'save_info': request.POST.get('save_info'),
            'username': str(request.user),
        })    
        return HttpResponse(status=200)
    except Exception as e:
        print(f"Error in cache_checkout_data: {e}")  # Debug print
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=str(e), status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Get cart from database instead of session
        cart = get_or_create_cart(request)
        
        if not cart.items.exists():
            messages.error(request, "Your cart is empty.")
            return redirect(reverse('books'))

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],          
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            
            # Create original_bag from cart items
            cart_data = {}
            for item in cart.items.all():
                if item.book.isbn not in cart_data:
                    cart_data[item.book.isbn] = {}
                cart_data[item.book.isbn][item.format] = item.quantity
            order.original_bag = json.dumps(cart_data)
            order.save()
            
            # Create order line items from cart
            for cart_item in cart.items.all():
                try:
                    order_line_item = OrderLineItem(
                        order=order,
                        book=cart_item.book,
                        quantity=cart_item.quantity,
                        format=cart_item.format,
                    )
                    order_line_item.save()
                except Exception as e:
                    messages.error(request, f"Error processing your order: {str(e)}")
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Clear the cart after successful order
            cart.clear()
            
            print(f"=== ORDER CREATED SUCCESSFULLY ===")  # Debug print
            print(f"Order number: {order.order_number}")  # Debug print
            print(f"Redirecting to checkout_success")  # Debug print
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')

    else:
        # Get cart from database instead of session
        cart = get_or_create_cart(request)
        
        if not cart.items.exists():
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('books'))
        
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)
    
    
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    print(f"=== CHECKOUT SUCCESS VIEW CALLED ===")  # Debug print
    print(f"Order number: {order_number}")  # Debug print
    
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    
    print(f"Order found: {order}")  # Debug print
    print(f"Order email: {order.email}")  # Debug print

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Send confirmation email immediately
    print(f"=== CALLING SEND_CONFIRMATION_EMAIL ===")  # Debug print
    email_sent = send_confirmation_email(order)
    print(f"Email sent result: {email_sent}")  # Debug print
    
    if email_sent:
        messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email has been sent to {order.email}.')
    else:
        messages.success(request, f'Order successfully processed! Your order number is {order_number}. We will send a confirmation email to {order.email} shortly.')
        messages.warning(request, 'There was an issue sending the confirmation email, but your order was processed successfully.')

    # Clean up session data
    if 'bag' in request.session:
        del request.session['bag']
    if 'save_info' in request.session:
        del request.session['save_info']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

