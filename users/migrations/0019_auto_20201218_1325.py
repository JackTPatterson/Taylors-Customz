# Generated by Django 3.1 on 2020-12-18 13:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20201218_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orderId',
            field=models.IntegerField(null=True, unique=True, verbose_name='Order Id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 18, 13, 25, 57, 537181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='orderNumber',
            field=models.IntegerField(null=True, unique=True, verbose_name='Order Number'),
        ),
    ]
