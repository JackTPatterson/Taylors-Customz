# Generated by Django 3.1 on 2020-12-18 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20201218_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shoe_size',
        ),
        migrations.AlterField(
            model_name='product',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 18, 13, 18, 31, 590872, tzinfo=utc)),
        ),
    ]
