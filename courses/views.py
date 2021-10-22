from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Course

# Create your views here.


def courses(request):
    courses = Course.objects.order_by('-start_date').filter(is_published=True)

    paginator = Paginator(courses, 6)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)

    context = {
        'courses': paged_courses
    }
    return render(request, 'courses/courses.html', context)


def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course
    }
    return render(request, 'courses/course.html', context)
