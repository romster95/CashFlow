from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'balance')
    #list_display_links =
    search_fields = ('name', 'id', 'email')
    list_filter = ('name', 'id')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # list_display_links =
    search_fields = ('name',)
    list_filter = ('name', 'id')

admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)

