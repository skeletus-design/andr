# Generated by Django 5.0 on 2023-12-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_coins_old_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=1000)),
                ('coins', models.IntegerField(default=1)),
            ],
        ),
    ]
