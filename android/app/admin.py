from django.contrib import admin

from .models import Coins, Wallet

@admin.register(Coins)
class LikesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'old_price', 'price', 'time']
    
@admin.register(Wallet)
class LikesAdmin(admin.ModelAdmin):
    list_display = ['id', 'money', 'coins']
