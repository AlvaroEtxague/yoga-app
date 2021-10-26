from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course'),
    path('<int:pk>/content/', views.CourseContentView.as_view(),
         name='course_content'),
    path('checkout/', views.CheckoutSession.as_view(), name='checkout'),
    path('checkout-success/', views.CheckoutSuccess.as_view(),
         name='checkout_success'),
    path('checkout-cancel/', views.CheckoutCancel.as_view(),
         name='checkout_cancel'),
    path('webhook/', views.stripe_webhook, name="stripe_webhook")
]
