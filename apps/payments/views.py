from django.shortcuts import render
# Create your views here.
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Price , Product

stripe.api_key = 'sk_test_51LXmPhI1Paqp8Qt3Tca8GhuEe1FI2bKbkscog7ORAiGRL00QsAKVgMaSwQ8RXUnM4Y3GwVC2BHLdZwoswI8dY0ax00GBNzBHsK'


class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/payments/success/',
            cancel_url='http://localhost:8000/payments/cancel/',
        )
        return redirect(checkout_session.url)
    
class HomePageView(TemplateView):
    template_name = "payments/home.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="IPHONE 11")
        prices = Price.objects.filter(product=product)
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context    
    

class SuccessView(TemplateView):
    template_name = "payments/success.html"


class CancelView(TemplateView):
    template_name = "payments/cancel.html"    