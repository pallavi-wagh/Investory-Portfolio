from django.db import models
from django.contrib.auth.models import User

class Investment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    annual_return = models.DecimalField(max_digits=50, decimal_places=2)
    payment_price=models.IntegerField()
    razor_pay_order_id= models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id= models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_signature= models.CharField(max_length=100, null=True, blank=True)
    # Add fields for 3yr, 5yr, 10yr returns

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    Name=models.CharField(max_length=20, blank=True, null=True)
    password=models.CharField(max_length=10, blank=True, null=True)
    