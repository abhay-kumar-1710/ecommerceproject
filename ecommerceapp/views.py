from django.shortcuts import render, redirect
from ecommerceapp.models import Customer, Product, AddToCart, OrderPlaced
from ecommerceapp.forms import LogInForm, RegisterForm, MyPasswordChangeForm, MyPasswordRestForm, MySetPasswordForm, CustomerForm
from django.views.generic import View, TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
import stripe # type: ignore

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

# AUTH VIEWS
    
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "ecommerceapp/registeration.html", {'form' : form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, "ecommerceapp/registeration.html", {'form' : form})
  
# PROJECT VIEWS

# HOME
def Home(request):
    random_obj = Product.objects.order_by('?')[:10]
    random_obj2 = Product.objects.order_by('?')[:10]
    top_shirts = Product.objects.filter(category = "Top Wear").filter(discounted_price__lt = 1100).order_by('?')[:8]
    mobile_offers = Product.objects.filter(category = "Mobile").filter(discounted_price__lt = 25000).order_by('?')[:8]
    return render(request, 'ecommerceapp/home.html', {'random_obj' : random_obj,
        'random_obj2' : random_obj2,
        'top_shirts' : top_shirts,
        'mobile_offers' : mobile_offers})

# LAPTOP
def Laptop(request, data = None):
    if data == None:
        laptops = Product.objects.filter(category = "Laptop")
    elif data == "hplaptop":
        laptops = Product.objects.filter(category = "Laptop").filter(brand = "HP")
    elif data == "acer":
        laptops = Product.objects.filter(category = "Laptop").filter(brand = "Acer")
    elif data == "lessthan30k":
        laptops = Product.objects.filter(category = "Laptop").filter(discounted_price__lt = 30000)
    elif data == "greatthan30k":
        laptops = Product.objects.filter(category = "Laptop").filter(discounted_price__gt = 30000)
    return render(request, 'ecommerceapp/laptop.html', {'laptops':laptops})

# MOBILE
def Mobile(request, data = None):
    if data == None:
        mobiles = Product.objects.filter(category = "Mobile")
    elif data == "redmi":
        mobiles = Product.objects.filter(category = "Mobile").filter(brand = "Redmi")
    elif data == "apple":
        mobiles = Product.objects.filter(category = "Mobile").filter(brand = "Apple")
    elif data == "lessthan25k":
        mobiles = Product.objects.filter(category = "Mobile").filter(discounted_price__lt = 25000)
    elif data == "greatthan25k":
        mobiles = Product.objects.filter(category = "Mobile").filter(discounted_price__gt = 25000)
    return render(request, 'ecommerceapp/mobile.html', {'mobiles':mobiles})

# TOPWEAR
def Topwear(request, data = None):
    if data == None:
        topwears = Product.objects.filter(category = "Top Wear")
    elif data == "roadster":
        topwears = Product.objects.filter(category = "Top Wear").filter(brand = "Roadster")
    elif data == "USPOLO":
        topwears = Product.objects.filter(category = "Top Wear").filter(brand = "US POLO")
    elif data == "lessthan1k":
        topwears = Product.objects.filter(category = "Top Wear").filter(discounted_price__lt = 1000)
    elif data == "greatthan1k":
        topwears = Product.objects.filter(category = "Top Wear").filter(discounted_price__gt = 1000)
    return render(request, 'ecommerceapp/topwear.html', {'topwears':topwears})

# BOTTOMWEAR
def Bottomwear(request, data = None):
    if data == None:
        bottomwears = Product.objects.filter(category = "Bottom Wear")
    elif data == "wrogn":
        bottomwears = Product.objects.filter(category = "Bottom Wear").filter(brand = "WROGN")
    elif data == "highlander":
        bottomwears = Product.objects.filter(category = "Bottom Wear").filter(brand = "HIGHLANDER")
    elif data == "lessthan1k":
        bottomwears = Product.objects.filter(category = "Bottom Wear").filter(discounted_price__lt = 1000)
    elif data == "greatthan1k":
        bottomwears = Product.objects.filter(category = "Bottom Wear").filter(discounted_price__gt = 1000)
    return render(request, 'ecommerceapp/bottomwear.html', {'bottomwears':bottomwears})

# PROFILE
class Profile(LoginRequiredMixin, FormView):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'ecommerceapp/profile.html', {'form':form})
    
    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            form.save()
            return redirect('showaddress')
        return render(request, 'ecommerceapp/profile.html', {'form':form})
        
# ADDRESS
@login_required
def Address(request):
    address = Customer.objects.all().filter(user=request.user)
    return render(request, 'ecommerceapp/showaddress.html', {'address' : address})

# PRODUCT DETAILS
def Productdetails(request, id):
    product = Product.objects.get(pk = id)
    items_already_in_cart = False
    if request.user.is_authenticated:
        items_already_in_cart = AddToCart.objects.filter(Q(product = Product.objects.get(pk = id)) & Q(user = request.user))
    return render(request, 'ecommerceapp/productdetails.html', {'product':product, 'items_already_in_cart' : items_already_in_cart})

# SHOW CART
@login_required
def Showcart(request):
    showcart = AddToCart.objects.all().filter(user = request.user)
    amount = 0
    shipping = 70
    if showcart:
        for i in showcart:
            tempamount = i.quantity * i.product.discounted_price
            amount += tempamount
        totalamount = amount + shipping
        return render(request, 'ecommerceapp/showcart.html', {'showcart':showcart, 'amount' : amount, 'totalamount' : totalamount})
    else:
        return render(request, 'ecommerceapp/emptycart.html')

# PLUS CART
@login_required # type: ignore
def Pluscart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        cart = AddToCart.objects.all().filter(user = request.user)
        c = AddToCart.objects.get(Q(user = request.user) & Q(product = prod_id))
        c.quantity += 1
        c.save()
        amount = 0
        shipping = 70
        for i in cart:
            tempamount = i.quantity * i.product.discounted_price
            amount += tempamount
            totalamount = amount + shipping
        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }
        return JsonResponse(data)
    
# MINUS CART
@login_required # type: ignore
def Minuscart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        cart = AddToCart.objects.all().filter(user = request.user)
        c = AddToCart.objects.get(Q(user = request.user) & Q(product = prod_id))
        c.quantity -= 1
        c.save()
        amount = 0
        shipping = 70
        for i in cart:
            tempamount = i.quantity * i.product.discounted_price
            amount += tempamount
            totalamount = amount + shipping
        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }
        return JsonResponse(data)
    
# REMOVE CART
@login_required # type: ignore
def Removecart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        cart = AddToCart.objects.all().filter(user = request.user)
        c = AddToCart.objects.get(Q(user = request.user) & Q(product = prod_id))
        c.delete()
        amount = 0
        shipping = 70
        for i in cart:
            tempamount = i.quantity * i.product.discounted_price
            amount += tempamount
        totalamount = amount + shipping
        data = {
            'amount' : amount,
            'totalamount' : totalamount
        }
        return JsonResponse(data)

# ADD TO CART
@login_required
def Addtocart(request, id):
    product = Product.objects.get(pk = id)
    add_to_cart = AddToCart(user = request.user, product = product, quantity = 1)
    add_to_cart.save()
    return redirect('/productdetails/'+ str(id))

@login_required
def Buynow(request, id):
    product = Product.objects.get(pk = id)
    add_to_cart = AddToCart(user = request.user, product = product, quantity = 1)
    add_to_cart.save()
    return redirect('/checkout/')

# CHECKOUT
@login_required # type: ignore
def Checkout(request):
    showcart = AddToCart.objects.all().filter(user = request.user)
    customer = Customer.objects.filter(user = request.user)
    amount = 0
    shipping = 70
    if showcart:
        for i in showcart:
            tempamount = i.quantity * i.product.discounted_price
            amount += tempamount
        totalamount = amount + shipping
        return render(request, 'ecommerceapp/checkout.html', {'showcart':showcart, 'amount' : amount, 'totalamount' : totalamount, 'customer' : customer})
    else:
        return render(request, 'ecommerceapp/emptycheckout.html')

# PAYMENT DONE
@login_required
def Paymentdone(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id = custid)
    cart = AddToCart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user = user, customer = customer, product = c.product, quantity = c.quantity).save()
        c.delete()
    return redirect('/orders/')

@login_required
def Orders(request):
    orders = OrderPlaced.objects.all().filter(user = request.user)
    if orders:
        return render(request, 'ecommerceapp/orders.html', {'orders' : orders})
    else:
        return render(request, 'ecommerceapp/emptyorders.html')