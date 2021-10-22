from .models import Course
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

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


class CheckoutSession(View):
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=request.POST.get('course'))

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
        except Exception as e:
            print(e)
            return str(e)
        return HttpResponseRedirect(checkout_session.url)


class CheckoutSuccess(TemplateView):
    template_name = "courses/checkout_success.html"


class CheckoutCancel(TemplateView):
    template_name = "courses/checkout_success.html"


def fulfill_order(session):
    # TODO: fill me in
    print("Fulfilling order", session)


@csrf_exempt
def stripe_webhook(request):
    print("#"*20)
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

        # Fulfill the purchase...
        fulfill_order(session)

    # Passed signature verification
    return HttpResponse(status=200)
