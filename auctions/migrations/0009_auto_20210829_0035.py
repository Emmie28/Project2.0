# Generated by Django 3.2.5 on 2021-08-28 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='listed_by',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 29, 0, 35, 6, 628486)),
        ),
    ]