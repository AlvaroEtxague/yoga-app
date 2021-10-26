from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, TemplateView, DetailView, ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
import stripe


from accounts.models import StripeTransaction
from .models import Course

stripe.api_key = settings.STRIPE_SECRET_KEY


class CourseListView(ListView):
    template_name = 'courses/courses.html'
    queryset = Course.objects.order_by('-start_date').filter(is_published=True)
    context_object_name = "courses"
    paginate_by = 6


class CourseDetailView(DetailView):
    template_name = 'courses/course.html'
    queryset = Course.objects.filter(is_published=True)


class CourseContentView(LoginRequiredMixin, DetailView):
    template_name = "courses/contents.html"

    def get_queryset(self):
        queryset = Course.objects.filter(
            students__in=[self.request.user])
        return queryset


class CheckoutSession(View):

    def post(self, request, *args, **kwargs):
        course_id = request.POST.get('course')
        # Check logged in or not
        if not request.user.is_authenticated:
            messages.error(request, "Please login to continue")
            next = reverse('course', args=[course_id])
            return redirect(f'/accounts/login/?next={next}')
        course = get_object_or_404(Course, id=course_id)

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {

                        'name': course.title,
                        'description': course.description,
                        'quantity': 1,
                        'currency': 'EUR',
                        'amount':  int(course.price * 100),
                    }
                ],
                payment_method_types=[
                    'card',
                ],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('checkout_success')),
                cancel_url=request.build_absolute_uri(
                    reverse('checkout_cancel'))
            )

            data = {
                "user": self.request.user,
                "course": course,
                "txn_id": checkout_session.get('id')
            }

            StripeTransaction.objects.create(**data)

        except Exception as e:
            return str(e)
        return HttpResponseRedirect(checkout_session.url)


class CheckoutSuccess(TemplateView):
    template_name = "courses/checkout_success.html"


class CheckoutCancel(TemplateView):
    template_name = "courses/checkout_success.html"


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        txn_obj = StripeTransaction.objects.filter(txn_id=session.id).first()
        if txn_obj:
            txn_obj.currency = session.currency
            txn_obj.amount = session.amount_total
            txn_obj.stripe_customer = session.customer
            txn_obj.is_paid = True
            txn_obj.add_student_to_course()
            txn_obj.save()
    # Passed signature verification
    return HttpResponse(status=200)
