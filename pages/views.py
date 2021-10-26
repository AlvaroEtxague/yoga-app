from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course
from teachers.models import Teacher

# Create your views here.


def index(request):
    courses = Course.objects.order_by(
        '-start_date').filter(is_published=True)[:3]

    context = {
        'courses': courses,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    teachers = Teacher.objects.order_by('-name')

    context = {
        'teachers': teachers,
    }
    return render(request, 'pages/about.html', context)
