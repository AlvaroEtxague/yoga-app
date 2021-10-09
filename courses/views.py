from django.shortcuts import render

# Create your views here.
def courses(request):
    return render(request, 'courses/courses.html')
    
def course(request):
    return render(request, 'courses/course.html')
    