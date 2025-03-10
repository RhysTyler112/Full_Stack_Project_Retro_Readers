from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="books"),
    path('<int:isbn>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
]