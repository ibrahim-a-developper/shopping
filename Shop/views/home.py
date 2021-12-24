from django.shortcuts import redirect, render
from Shop.models import Category, Product
from django.views import View

class Index(View):
    def post(self, request):
        product= request.POST.get('product')
        remove= request.POST.get('remove')
        cart= request.session.get('cart')
      
        if cart:
          
            quantity= cart.get(product)
            #print(quantity , cart)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                    
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart= {}
            cart[product] = 1
        
        request.session['cart'] = cart
        return redirect("home_page")
    
    def get(self, request):
        cart= request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
            
        products= None
        categories= Category.get_all_categories()
        categoryID= request.GET.get('category')

        if categoryID:
            products= Product.get_all_products_by_categoryid(categoryID)
            # products=Product.objects.filter(category = categoryID)
        else:
            products= Product.get_all_products()

        data= {}
        data['products' ]= products
        data['categories' ]= categories
        return render(request, 'index.html', data)