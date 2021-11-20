from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's no items in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JizYmGk6ZOsZ5tM42UVZKf8zrQWQ7oMm2CFFFl67hxzu9grFwlYIxmuvSalqAzTAfc0VwO6mqoCKMkZ0lbqQxuA003mSZeRAf',
    }

    return render(request, template, context)