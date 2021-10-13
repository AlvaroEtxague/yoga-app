from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.

def contact(request):
    if request.method == 'POST':
        course_id = request.POST['course_id']
        course = request.POST['course']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        teacher_email = request.POST['teacher_email']
        
        
        # check if user already made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
            course_id=course_id, user_id=user_id)
            
            if has_contacted:
                messages.error(
                request, "You already made an inquiry for this listing.")
                return redirect('/courses/'+course_id)
        
        contact = Contact(
            course=course, course_id=course_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        
        contact.save()
        
        # send email
        send_mail('Yoga Course Inquiry','There has been an inquiry for ' + course + '. Sign into the admin panel for more info.','primaryemail@test.com',[teacher_email, 'secondaryemail@test.com'],fail_silently=False)
        
        messages.success(request, "Your request has been submitted, a teacher will get back to you shortly.")
        return redirect('/courses/'+course_id)
