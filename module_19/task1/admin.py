from django.contrib import admin
from .models import *

admin.site.register(News)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')
    list_display = ('username', 'balance', 'age')
    search_fields = ('username',)
    list_per_page = 30
    readonly_fields = ('balance',)
