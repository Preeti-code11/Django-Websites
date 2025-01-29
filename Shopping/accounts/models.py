from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Make email unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    address = models.TextField(blank=True, null=True)  # Optional field for user address
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Profile picture

    def __str__(self):
        return self.email  # Display email as the primary identifier

