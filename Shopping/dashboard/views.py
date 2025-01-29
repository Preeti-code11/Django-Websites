from django.shortcuts import render
from orders.models import Order
from payment.models import Payment
from shop.models import Product
from django.contrib.auth.decorators import login_required, user_passes_test

# Helper function to restrict access to admins
def admin_only(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(admin_only)
def dashboard_home(request):
    total_orders = Order.objects.count()
    total_payments = Payment.objects.count()
    total_products = Product.objects.count()
    total_users = request.user.__class__.objects.filter(is_staff=False).count()

    context = {
        'total_orders': total_orders,
        'total_payments': total_payments,
        'total_products': total_products,
        'total_users': total_users,
    }
    return render(request, 'dashboard/home.html', context)

