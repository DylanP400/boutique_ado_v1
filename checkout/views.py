from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Theres nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NijGEG0YbSkG1G8MPL4O1bcY1VLkW4csS6IkFkCNiVvTY8BOOwHY4guVEfALb5bBTd2sqADO0JVEjnN0vOrEIpU00xsrfxJeo',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)