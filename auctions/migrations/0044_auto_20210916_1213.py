# Generated by Django 3.2.5 on 2021-09-16 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0043_auto_20210916_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 12, 13, 55, 971220)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 12, 13, 55, 971220)),
        ),
        migrations.AlterField(
            model_name='listdetails',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 12, 13, 55, 971220)),
        ),
    ]