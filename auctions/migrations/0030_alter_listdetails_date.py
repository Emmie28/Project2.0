# Generated by Django 3.2.5 on 2021-09-07 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_alter_listdetails_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listdetails',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 15, 55, 13, 380445)),
        ),
    ]
