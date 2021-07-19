import uuid

from django.contrib.auth import get_user_model
from django.db import models


# Deposit
class Deposit(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name='deposits', on_delete=models.CASCADE)
    address = models.CharField(max_length=48)
    amount = models.DecimalField(max_digits=8, decimal_places=4)
    asset = models.CharField(max_length=48, choices=(
        ('Bitcoin', 'Bitcoin'),
        ('Ethereum', 'Ethereum'),
        ('Dogecoin', 'Dogecoin'),
        ('Litecoin', 'Litecoin')
    ))
    date = models.DateField()
    time = models.TimeField()
    has_been_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=48, default='pending', choices=(
        ('pending', 'Pending'),
        ('declined', 'Declined'),
        ('verified', 'Verified'),
        ('credited', 'Credited')
    ))
    processed = models.BooleanField(default=False, editable=False)
    txref = models.UUIDField(default=uuid.uuid4, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "Deposit {0}".format(self.id)


# Withdrawal
class Withdrawal(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name='withdrawals', on_delete=models.CASCADE)
    address = models.CharField(max_length=48)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    asset = models.CharField(max_length=48, choices=(
        ('Bitcoin', 'Bitcoin'),
        ('Ethereum', 'Ethereum'),
        ('Dogecoin', 'Dogecoin'),
        ('Litecoin', 'Litecoin')
    ))
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=48, default='pending', choices=(
        ('pending', 'Pending'),
        ('declined', 'Declined'),
        ('paid', 'Paid')
    ))
    has_been_settled = models.BooleanField(default=False)
    processed = models.BooleanField(default=False, editable=False)
    txref = models.UUIDField(default=uuid.uuid4, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "Withdrawal {0}".format(self.id)

# User Wallet


class UserWallet(models.Model):
    user = models.OneToOneField(
        get_user_model(), related_name='wallet', on_delete=models.CASCADE)
    balance = models.PositiveBigIntegerField(default=0)

    def decrease(self, amt):
        if amt > self.balance:
            return False
        self.balance -= amt
        self.save()
        return True

    def balance_string(self):
        return self.balance

    def increase(self, amt):
        self.balance += amt
        self.save()

    def __str__(self):
        return "{0}'s wallet".format(self.user.get_full_name())
