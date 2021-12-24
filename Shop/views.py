from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Create your views here.
def index(request):
    products= None
    categories= Category.get_all_categories()
    categoryID= request.GET.get('category')
    
    if categoryID:
        products= Product.get_all_products_by_categoryid(categoryID)
        # products=Product.objects.filter(category = categoryID)
    else:
        products= Product.get_all_products()

    data= {}
    data['products']= products
    data['categories']= categories
    return render(request, 'index.html', data)

def validationCustomer(customer):

      #validation
        error_message=None
        if(not customer.first_name):
            error_message='First name required'
        elif(len(customer.first_name) < 4):
            error_message= 'First name must 4 char long or more'
        if (not customer.last_name):
            error_message = 'Last name required'
        elif (len(customer.last_name) < 4):
            error_message = 'Last name must 4 char long or more'
        if (not customer.phone):
            error_message = 'Phone name required'
        elif (len(customer.phone) < 4):
            error_message = 'Phone name must 4 char long or more'
        elif (len(customer.password) < 6):
            error_message = 'Password name must 6 char long or more'
        elif customer.isExists():
            error_message="Email adesse has exist"
       

def registerUser(request):
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')

    customer = Customer(first_name = first_name,
                        last_name = last_name,
                        phone = phone, email = email,
                        password = make_password(password))

    value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,

        }
    error_message= validationCustomer(customer)

        #saving
    if(not error_message):
        # customer.password=make_password(customer.password)
        customer.register()
        return redirect('home_page')
    else:
        data= {
                'error':error_message,
                'values': value,
            }

        return render(request, 'signup.html', data)


def signup(request):
    # print(check_password('123456789', 'pbkdf2_sha256$180000$2McpJylE0XGQ$IE7Z2LLdIXGisrUoO2r0Hf74Mio4Kw6gN/3R1sxTFp8='))
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)
   


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer= Customer.get_customer_by_email(email)
        if customer:
            flag=check_password(password, customer.password)
            if flag:
                return redirect('home_page')
            else:
                error_message="password false"
        else:
            error_message="Email not exists"
        return render(request, 'login.html', {'error': error_message})
    

           
