# Generated by Django 3.1 on 2020-12-19 03:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20201219_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='message',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 19, 3, 47, 20, 833019, tzinfo=utc)),
        ),
    ]
