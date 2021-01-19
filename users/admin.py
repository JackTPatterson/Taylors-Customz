from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, AboutMe, Reviews, Pictures
# Register your models here.
admin.site.register(Product)
admin.site.unregister(Group)
admin.site.register(AboutMe)
admin.site.register(Reviews)
admin.site.register(Pictures)