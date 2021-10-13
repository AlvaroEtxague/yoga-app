from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'email',
                    'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'course')
    list_per_page = 25


# Register your models here.
admin.site.register(Contact, ContactAdmin)