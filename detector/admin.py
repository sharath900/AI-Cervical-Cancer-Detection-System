from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Columns shown in admin list
    search_fields = ('name', 'email', 'message')   # Adds a search bar
    readonly_fields = ('created_at',)               # Prevents tampering with timestamps