from django.contrib import admin

from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_per_page = 20

admin.site.register(Teacher, TeacherAdmin)
