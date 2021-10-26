from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html",
                                      redirect_authenticated_user=True),
         name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashBoardView.as_view(), name='dashboard'),
]
