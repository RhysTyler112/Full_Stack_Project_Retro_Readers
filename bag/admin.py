from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'get_total_items', 'get_total_cost', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'session_key')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CartItemInline]
    
    def get_total_items(self, obj):
        return obj.get_total_items()
    get_total_items.short_description = 'Total Items'
    
    def get_total_cost(self, obj):
        return f"£{obj.get_total_cost():.2f}"
    get_total_cost.short_description = 'Total Cost'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'book', 'format', 'quantity', 'get_total_price', 'created_at')
    list_filter = ('format', 'created_at', 'updated_at')
    search_fields = ('book__title', 'book__isbn', 'cart__user__username')
    readonly_fields = ('created_at', 'updated_at')
    
    def get_total_price(self, obj):
        return f"£{obj.get_total_price():.2f}"
    get_total_price.short_description = 'Total Price'
