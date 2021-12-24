from django.shortcuts import render, redirect
from django.views import View
from Shop.models.order import  Order





class OrderView(View):
  
    def get(self, request):
        customer= request.session.get('customer')
        orders= Order.get_orders_by_customer(customer)
        print(orders)
        # orders= orders.reverse()pour tri comme order_by()
        return render(request, 'orders.html', {'orders': orders})

