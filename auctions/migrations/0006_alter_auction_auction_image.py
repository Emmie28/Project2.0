# Generated by Django 3.2.5 on 2021-08-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_auction_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]