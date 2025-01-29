from django.shortcuts import render
from django.conf import settings
import razorpay

def initiate_payment(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
    order = client.order.create({
        "amount": 50000,  # Amount in paise
        "currency": "INR",
        "payment_capture": "1"
    })
    context = {
        'razorpay_order_id': order['id'],
        'razorpay_key': settings.RAZORPAY_API_KEY,
        'amount': 500.00,  # Amount in INR
    }
    return render(request, 'payment/initiate_payment.html', context)

