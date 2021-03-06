# Generated by Django 3.1 on 2020-12-15 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201214_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orderId',
            field=models.IntegerField(null=True, verbose_name='Order Id'),
        ),
        migrations.AddField(
            model_name='product',
            name='orderNumber',
            field=models.IntegerField(null=True, verbose_name='Order Number'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 13, 18, 11, 379962, tzinfo=utc)),
        ),
    ]
