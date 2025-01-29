from django.shortcuts import render, redirect, get_object_or_404
from .models import Address, ShippingDetails
from django.contrib.auth.decorators import login_required

@login_required
def add_address(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        street_address = request.POST['street_address']
        city = request.POST['city']
        state = request.POST['state']
        postal_code = request.POST['postal_code']
        country = request.POST['country']

        Address.objects.create(
            user=request.user,
            full_name=full_name,
            phone=phone,
            street_address=street_address,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
        )
        return redirect('address_list')

    return render(request, 'shipping/add_address.html')

@login_required
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'shipping/address_list.html', {'addresses': addresses})

