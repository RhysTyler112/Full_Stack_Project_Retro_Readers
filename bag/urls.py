from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<str:isbn>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<str:isbn>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<str:isbn>/', views.remove_from_bag, name='remove_from_bag'),
]