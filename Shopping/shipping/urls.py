from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_address, name='add_address'),
    path('list/', views.address_list, name='address_list'),
]
