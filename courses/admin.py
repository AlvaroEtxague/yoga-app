from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('teacher',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_per_page = 20

admin.site.register(Course, CourseAdmin)
