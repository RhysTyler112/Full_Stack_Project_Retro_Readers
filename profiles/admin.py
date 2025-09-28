from django.contrib import admin
from .models import UserProfile, Wishlist


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_country', 'default_town_or_city')
    list_filter = ('default_country',)
    search_fields = ('user__username', 'user__email', 'default_phone_number')
    ordering = ('user__username',)


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    list_filter = ('book__category',)
    search_fields = ('user__username', 'book__title', 'book__author')
    ordering = ('user__username', 'book__title')
