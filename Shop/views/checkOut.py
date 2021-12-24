from django.shortcuts import render, redirect
from django.views import View
from Shop.models import Product, Order
from Shop.models.customer import Customer


class CheckOut(View):
    def post(self, request):
        adresse = request.POST.get('adresse')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_by_product(list(cart.keys()))
        for product in products:
        
            order = Order(customer=Customer(id=customer),
                          adresse=adresse,
                          product=product,
                          phone=phone,
                          price=product.price,
                          quantity=cart.get(str((product.id))))
            
            order.save()
        request.session['cart']={}
        print(adresse, phone, customer, cart)
        return redirect('cart')
