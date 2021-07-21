# Generated by Django 3.2.5 on 2021-07-21 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import services.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=48)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('asset', models.CharField(choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Dogecoin', 'Dogecoin'), ('Litecoin', 'Litecoin')], max_length=48)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('declined', 'Declined'), ('paid', 'Paid')], default='pending', max_length=48)),
                ('has_been_settled', models.BooleanField(default=False)),
                ('processed', models.BooleanField(default=False, editable=False)),
                ('txref', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveBigIntegerField(default=0)),
                ('btc_balance', models.DecimalField(decimal_places=12, default=0, max_digits=20)),
                ('btc_address', models.CharField(default=services.models.get_btc_addr, max_length=48, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=48)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=8)),
                ('asset', models.CharField(choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Dogecoin', 'Dogecoin'), ('Litecoin', 'Litecoin')], max_length=48)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('has_been_verified', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('declined', 'Declined'), ('verified', 'Verified'), ('credited', 'Credited')], default='pending', max_length=48)),
                ('processed', models.BooleanField(default=False, editable=False)),
                ('txref', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
