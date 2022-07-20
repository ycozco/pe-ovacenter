import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Membership(models.Model):
    membership_name = models.CharField(max_length =100)
    membership_description =  models.CharField(max_length = 240)
    membership_price_1_month= models.CharField(max_length=8)
    membership_price_3_month= models.CharField(max_length=8)
    membership_price_6_month= models.CharField(max_length=8)
    membership_price_12_month= models.CharField(max_length=8)
    membership_price_24_month= models.CharField(max_length=8)
    membership_image  = models.ImageField(upload_to='membership_images/', blank=True)

    def __str__(self) -> str:
        return self.member_name

class Routine(models.Model):
    routine_name = models.CharField(max_length =100)
    routine_description = models.CharField(max_length =100)
    routine_date = models.DateField()
    routine_duration = models.TimeField()   

    def __str__(self) -> str:
        return self.routine_name

class Ovauser(models.Model):
    Ovauser_name = models.CharField(max_length =100)
    Ovauser_password =  models.CharField(max_length = 8)
    Ovauser_email =  models.EmailField()
    Ovauser_phone = models.CharField(max_length = 10)
    Ovauser_dni =  models.CharField(max_length = 8)
    Ovauser_birthday = models.DateField()
    Ovauser_fingerprint = models.ImageField(upload_to='fingerprint_images/', blank=True)

    Ovamembership_id = models.ForeignKey(Membership, on_delete=models.CASCADE)
    Ovaroutine_id = models.ForeignKey(Routine, on_delete=models.CASCADE)
    Ovauser_membership_ini = models.DateField()
    Ovauser_membership_end = models.DateField()

    def __str__(self) -> str:
        return self.user_name

class Product(models.Model):
    product_name = models.CharField(max_length =100)
    product_description = models.CharField(max_length =100)
    product_price = models.CharField(max_length =8)
    product_image = models.ImageField(upload_to='product_images/', blank=True)

    def __str__(self) -> str:
        return self.product_name

class Ovauser_debt(models.Model):
    Ovauser_debt_Ovauser_id = models.ForeignKey(Ovauser, on_delete=models.CASCADE)
    Ovauser_debt_date = models.DateField()
    Ovauser_debt_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Ovauser_debt_description = models.CharField(max_length =100)

    def __str__(self) -> str:
        return self.Ovauser_debt_Ovauser_id








