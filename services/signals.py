from django.contrib.auth import authenticate, get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Deposit, UserWallet, Withdrawal


@receiver(post_save, sender=get_user_model(), dispatch_uid='add_wallet')
def add_wallet(sender, **kwargs):
    user = kwargs.get('instance')

    if not UserWallet.objects.filter(user=user).exists():
        new_wallet = UserWallet.objects.create(user=user)
        new_wallet.save()


@receiver(post_save, sender=Deposit, dispatch_uid='add_amount')
def add_amount(sender, request=None, **kwargs):
    deposit = kwargs.get('instance')
    wallet = deposit.user.wallet

    if deposit.processed:
        return

    if deposit.has_been_verified:
        wallet.increase(deposit.amount)
        deposit.processed = True
        deposit.save()


@receiver(post_save, sender=Withdrawal, dispatch_uid='deduct_amount')
def deduct_amount(sender, request=None, **kwargs):
    withdrawal = kwargs.get('instance')
    wallet = withdrawal.user.wallet

    if withdrawal.processed:
        return

    if withdrawal.has_been_settled:
        wallet.decrease(withdrawal.amount)
        withdrawal.processed = True
        withdrawal.save()
