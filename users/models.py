from django.db import models
from django.db.models.fields.related import OneToOneField
from django.utils import timezone as tz


# Create your models here.
class Product(models.Model):
    shoe_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    description = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    shoe_size = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    hasShoe = models.CharField(max_length=100)

    date_submitted = models.DateTimeField(default=tz.now())

    orderNumber = models.IntegerField(verbose_name="Order Number", null=True, unique=True)
    orderId = models.IntegerField(verbose_name="Order Id", null=True, unique=True)
    completed = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    denied = models.BooleanField(default=False)
    price = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=255, blank=True)

    archived = models.BooleanField(default=False)

    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    postal = models.CharField(max_length=255, blank=True)

    def __str__(self):
       return f'{self.first_name.capitalize()}' + ' ' + f'{self.last_name.capitalize()}' + ' ➜ ' + f'{self.shoe_name}'
    
