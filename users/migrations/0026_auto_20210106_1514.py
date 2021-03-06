# Generated by Django 3.0.8 on 2021-01-06 20:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20210104_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 20, 14, 21, 411445, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='hasShoe',
            field=models.CharField(max_length=100),
        ),
    ]
