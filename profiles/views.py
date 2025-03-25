from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from books.models import Books

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, isbn):
    book = get_object_or_404(Books, isbn=isbn)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, book=book)
    if created:
        messages.success(request, f'Added {book.title} to your wishlist')
    else:
        messages.info(request, f'{book.title} is already in your wishlist')
    return redirect('book_detail', isbn=isbn)


@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    if not wishlist_items.exists():
        messages.info(request, 'Your wishlist is currently empty.')
    return render(request, 'profiles/wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def remove_from_wishlist(request, isbn):
    book = get_object_or_404(Books, isbn=isbn)
    wishlist_item = get_object_or_404(Wishlist, user=request.user, book=book)
    wishlist_item.delete()
    messages.success(request, f'Removed {book.title} from your wishlist')
    return redirect('view_wishlist')
