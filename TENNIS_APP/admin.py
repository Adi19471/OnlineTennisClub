from django.contrib import admin

# Register your models here.
from .models import Contact,OnlineBooking




admin.site.register(Contact)
admin.site.register(OnlineBooking)
class ContactAdmin(admin.ModelAdmin):
    list_display_links = ['name']
    
class OnlineBookingAdmin(admin.ModelAdmin):
    list_display_links = ['name']