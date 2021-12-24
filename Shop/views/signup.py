from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
# from .registerUser import registerUser
from .validation import validationCustomer
from ..models import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone, email=email,
                            password=make_password(password))

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,

        }
        error_message = validationCustomer(customer)

        # saving
        if (not error_message):
            # customer.password=make_password(customer.password)
            customer.register()
            return redirect('home_page')
        else:

            data = {
                'error': error_message,
                'values': value,
            }

            return render(request, 'signup.html', data)