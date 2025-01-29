from django.shortcuts import render
from django.views import View

def index(request):
    context = {
        'currencies': ['INR', 'GBP', 'CAD', 'USD', 'AUD', 'EUR', 'JPY'],
        'languages': ['German', 'French', 'English']
    }
    return render(request, 'shop/index.html', context)  # Update path if needed


def product(request, id):
    return render(request, 'shop/product.html', {'id': id})

def home(request):
  return render(request, 'shop/home.html')


def login(request):
 return render(request, 'shop/login.html')

def register(request):
 return render(request, 'shop/register.html')

def wishlist(request):
 return render(request, 'shop/wishlist.html')