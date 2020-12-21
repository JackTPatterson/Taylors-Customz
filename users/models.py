from django.db import models
from django.utils import timezone as tz

# Create your models here.
class Product(models.Model):
    shoe_name = models.CharField(max_length=100, null=False, blank=True)
    photo = models.ImageField(default='shoe.jpg', upload_to='media', blank=True)
    description = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    shoe_size = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(blank=True)
    hasShoe = models.BooleanField(blank=True, default=True)

    date_submitted = models.DateTimeField(default=tz.now())

    orderNumber = models.IntegerField(verbose_name="Order Number", null=True, unique=True)
    orderId = models.IntegerField(verbose_name="Order Id", null=True, unique=True)
    completed = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    denied = models.BooleanField(default=False)
    price = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=255, blank=True)

    def __str__(self):
       return f'{self.first_name.capitalize()}' + ' ' + f'{self.last_name.capitalize()}' + ' ➜ ' + f'{self.shoe_name}'
    
class Gallery(models.Model):
    shoe_name = models.CharField(max_length=100, null=False, blank=True)
    photo = models.ImageField(default='shoe.jpg', upload_to='media/gallery', blank=True)
    price = models.CharField(max_length=100, blank=True)
