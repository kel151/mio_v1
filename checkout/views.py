from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HXzJ4HBU1PUzPaEyzSwHxXGA4CBuGTdF6xC3wDW0C0eqm7deq6C8DxoR3IhPVDbcfYk7tjO0xeV8rCSiwX0kous00GA0N4pGw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)