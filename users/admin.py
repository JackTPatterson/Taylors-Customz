from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, AboutMe, Reviews, Pictures

admin.site.site_header = 'Taylors Customz'
admin.site.site_title = 'Taylors Customz'
admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'Admin'
admin.empty_value_display = '**Empty**'


# Register your models here.
admin.site.register(Product)
admin.site.unregister(Group)
admin.site.register(AboutMe)
admin.site.register(Reviews)
admin.site.register(Pictures)