from django.shortcuts import render, redirect
from .models import Order
from shop.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = Product.objects.get(id=product_id)
        order = Order.objects.create(user=request.user, product=product, quantity=quantity)
        return redirect('order_list')
    return render(request, 'orders/create_order.html')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

