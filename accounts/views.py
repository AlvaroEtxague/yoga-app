from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.contrib import messages, auth
from contacts.models import Contact
from courses.models import Course
from .forms import UserRegisterForm


class RegistrationView(CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        self.object = form.save()
        auth.login(self.request, self.object)
        messages.success(self.request, "You are now logged in")
        return redirect('index')


class DashBoardView(LoginRequiredMixin, ListView):
    template_name = "accounts/dashboard.html"

    def get_queryset(self):
        queryset = Contact.objects.filter(
            user_id=self.request.user.id).order_by(
            '-contact_date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bought_courses = Course.objects.filter(
            students__in=[self.request.user])
        context['bought_courses'] = bought_courses
        return context
