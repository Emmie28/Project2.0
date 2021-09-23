# Generated by Django 3.2.5 on 2021-08-23 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='new comment')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction')),
            ],
        ),
    ]
