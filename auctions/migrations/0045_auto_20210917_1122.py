# Generated by Django 3.2.5 on 2021-09-17 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0044_auto_20210916_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding',
            name='bidder_name',
            field=models.CharField(default='Your name', max_length=200),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 11, 22, 3, 463446)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 11, 22, 3, 465445)),
        ),
        migrations.AlterField(
            model_name='listdetails',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 11, 22, 3, 465445)),
        ),
    ]
