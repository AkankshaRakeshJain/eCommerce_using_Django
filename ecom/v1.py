from django.shortcuts import render

from ecom.models import *

# Create your views here. 
def home(request):
    product = Product.objects.all()
    categories = Category.objects.all()
    template = 'home.html'
    context = {'categories':categories,'product':product}
    return render(request,template,context)

def category(request,pk):
    categories = Category.objects.all()

    pk_category = Category.objects.get(id=pk)
    product = Product.objects.filter(category=pk_category)

    template = 'home.html'
    context = {'categories':categories,'product':product}
    return render(request,template,context)

def cart(request):
    template = 'cart.html'
    if request.user.is_authenticated:
        customer = request.user.customer #will allow you to access all the fields of the user model
        order,created = Order.objects.get_or_create(customer=customer,status=False)
        items = order.customerorder_set.all()
    else:
        items = []
        order = {'get_cart_total_items':0,'get_cart_total_price':0}

    context={'order':order,'items':items}
    return render(request,template,context)

def checkout(request):
    template = 'checkout.html'
    
    if request.user.is_authenticated:
        customer = request.user.customer #will allow you to access all the fields of the user model
        order,created = Order.objects.get_or_create(customer=customer,status=False)
        items = order.customerorder_set.all()
    else:
        items = []
        order = {'get_cart_total_items':0,'get_cart_total_price':0}

    context={'order':order,'items':items}
    return render(request,template,context)

def address(request):
    template = 'address.html'
    context = {}
    return render(request,template,context)

def payment(request):
    template = 'payment.html'
    context = {}
    return render(request,template,context)

# def updateToCart(request):
