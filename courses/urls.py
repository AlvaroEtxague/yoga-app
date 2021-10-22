from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:course_id>', views.course, name='course'),
    path('checkout/', views.CheckoutSession.as_view(), name='checkout'),
    path('checkout-success/', views.CheckoutSuccess.as_view(),
         name='checkout_success'),
    path('checkout-cancel/', views.CheckoutCancel.as_view(), name='checkout_cancel'),
    path('webhook/', views.stripe_webhook, name="stripe_webhook")
]
