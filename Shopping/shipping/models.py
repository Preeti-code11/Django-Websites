from django.db import models
from django.conf import settings

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addresses')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    street_address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default="India")
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}, {self.street_address}, {self.city}"

class ShippingDetails(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='shipping_details')
    order_id = models.CharField(max_length=100, unique=True)
    shipping_date = models.DateField()
    estimated_delivery_date = models.DateField()
    tracking_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ], default='Pending')

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"

