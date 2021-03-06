# Generated by Django 3.2.5 on 2021-09-08 11:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_alter_listdetails_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listdetails',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 13, 23, 51, 929962)),
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='auctions.auction')),
            ],
        ),
    ]
