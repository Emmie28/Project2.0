# Generated by Django 3.2.5 on 2021-09-07 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_alter_auction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding',
            name='bid_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 14, 8, 52, 41124)),
        ),
    ]