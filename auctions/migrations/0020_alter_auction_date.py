# Generated by Django 3.2.5 on 2021-09-06 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_auction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 22, 4, 39, 489341)),
        ),
    ]
