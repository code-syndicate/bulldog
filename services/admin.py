from django.contrib import admin

from .models import Deposit, UserWallet, Withdrawal

admin.site.register(UserWallet)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
