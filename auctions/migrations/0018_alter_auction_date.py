# Generated by Django 3.2.5 on 2021-09-06 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_auction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 19, 26, 59, 473615)),
        ),
    ]