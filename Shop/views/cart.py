from django.shortcuts import render, redirect
from django.views import View
from Shop.middlewars.auth import auth_middleware
from Shop.models import Product
# from   django.utils.decorators import method_decorator

class Cart(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        ids= list(request.session.get('cart').keys())
        products=Product.get_by_product(ids)
        return render(request, 'cart.html', {'products': products})
