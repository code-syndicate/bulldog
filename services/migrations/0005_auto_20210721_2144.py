# Generated by Django 3.2.5 on 2021-07-21 20:44

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_withdrawal_has_been_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwallet',
            name='btc_address',
            field=models.CharField(default=services.models.get_btc_addr, max_length=48, unique=True),
        ),
        migrations.AddField(
            model_name='userwallet',
            name='btc_balance',
            field=models.DecimalField(decimal_places=12, default=0, max_digits=20),
        ),
    ]
