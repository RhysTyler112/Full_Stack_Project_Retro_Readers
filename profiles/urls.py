from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlist/add/<str:isbn>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/remove/<str:isbn>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]