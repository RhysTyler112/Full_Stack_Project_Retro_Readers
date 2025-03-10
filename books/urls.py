from django.urls import path
from . import views

urlpatterns = [
   path('add/', views.add_book, name='add_book'),
    path('edit/<str:isbn>/', views.edit_book, name='edit_book'),
    path('<str:isbn>/', views.book_detail, name='book_detail'),
    path('', views.book_list, name='books'),
]