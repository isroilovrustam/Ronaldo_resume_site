from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']
    # list_filter = ['created_at']


admin.site.register(Contact)
