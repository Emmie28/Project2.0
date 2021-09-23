# Generated by Django 3.2.5 on 2021-08-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_auction_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='min_bid_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='auction',
            name='title',
            field=models.CharField(default='something new', max_length=200),
        ),
    ]
