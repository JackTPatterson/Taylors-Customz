# Generated by Django 3.1 on 2020-12-18 23:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20201218_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='started',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 18, 23, 24, 7, 427896, tzinfo=utc)),
        ),
    ]
