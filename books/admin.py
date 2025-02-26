from django.contrib import admin
from .models import Category, Books

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )
class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'realised_date',
    )
    ordering = ('category',)

admin.site.register(Category)
admin.site.register(Books)