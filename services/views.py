import uuid

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import mail
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from users.models import User, UserData, VerificationCode

from .forms import *
from .mails import mail_message
from .models import Deposit, UserWallet, Withdrawal


def generate_unique_code():
    code1 = uuid.uuid4().clock_seq
    code2 = uuid.uuid4().clock_seq
    code = str(code1) + str(code2)
    code = code[:7]
    if VerificationCode.objects.filter(code=code).count() > 1:
        return generate_unique_code()

    return code

    # Index View


class UploadIDView(LoginRequiredMixin, View):
    def post(self, request):
        id_file = request.FILES.get('ID', None)
        if id_file is None:
            context = {
                'message': "An error occured while uploading your ID.Please check and try again.", 'color': 'red'}
            return render(request, 'services/profile.html', context)

        request.user.has_uploaded_id = True
        request.user.save()
        context = {
            'message': "Your ID has been successfully uploaded!", 'color': 'green'}
        return render(request, 'services/dashboard.html', context)


class IndexView(View):
    def get(self, request):
        # if request.user.is_authenticated:
        #     return redirect('/dashboard/')
        context = {'formB': 'hidden', 'formA': 'block'}
        return render(request, 'services/index.html', context)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        context = {'bitcoinAddress': '3L3LnvfKMTVZcZJtTR7eLdoMzh4g8n1QyS', 'ethereumAddress': '0x9cbd14f198d4addad022beb882ad069ec2163a3c',
                   'dogecoinAddress': 'D8Kr7nbfG9ykqes5miiq78mfiF6Hf2XnmD', 'litecoinAddress': 'LT4o4VedSQrnCFQus8oPJWMRe2xnNQonUq'}
        return render(request, 'services/profile.html', context)


class WalletView(LoginRequiredMixin, View):
    def get(self, request):
        context = {'bitcoinAddress': '3L3LnvfKMTVZcZJtTR7eLdoMzh4g8n1QyS', 'ethereumAddress': '0x9cbd14f198d4addad022beb882ad069ec2163a3c',
                   'dogecoinAddress': 'D8Kr7nbfG9ykqes5miiq78mfiF6Hf2XnmD', 'litecoinAddress': 'LT4o4VedSQrnCFQus8oPJWMRe2xnNQonUq'}
        return render(request, 'services/wallet.html', context)


class FAQView(View):
    def get(self, request):
        context = {}
        return render(request, 'services/faq.html', context)


class ContactView(View):
    def get(self, request):
        context = {}
        return render(request, 'services/contact.html', context)


# Tx History
class HistoryView(LoginRequiredMixin,  View):
    login_url = '/authenticate-user/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        deposits = Deposit.objects.order_by('-time').order_by('-date').all()
        withdrawals = Withdrawal.objects.order_by('-time').order_by(
            '-date').all()
        context = {'withdrawals': withdrawals, 'deposits': deposits, 'bitcoinAddress': '3L3LnvfKMTVZcZJtTR7eLdoMzh4g8n1QyS', 'ethereumAddress': '0x9cbd14f198d4addad022beb882ad069ec2163a3c',
                   'dogecoinAddress': 'D8Kr7nbfG9ykqes5miiq78mfiF6Hf2XnmD', 'litecoinAddress': 'LT4o4VedSQrnCFQus8oPJWMRe2xnNQonUq'}
        return render(request, 'services/history.html', context)


# Verify Deposit View
class VerifyDepositView(LoginRequiredMixin, View):
    login_url = '/authenticate-user/'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        form = VerifyForm(request.POST)
        if form.is_valid():

            deposit = Deposit.objects.create(
                **form.cleaned_data, user=request.user)
            deposit.save()
            pass
            context = {
                'message': 'Your request has been placed, you will receive a confirmation email immediately your claim is confirmed.', 'color': 'green'}
            return render(request, 'services/dashboard.html', context)
        else:
            errors = ''
            for field in form:
                if not(field.errors):
                    continue
                error = '<span>{0} '.format(
                    field.label)
                for ferror in field.errors:
                    error += '<br> <span class = "text-base">  {0} </span>'.format(
                        ferror)
                errors += '<br>{0} </span'.format(error)

            context = {'message': errors, 'color': 'red'}
            return render(request, 'services/dashboard.html', context)


# Withdraw View
class WithdrawView(LoginRequiredMixin, View):
    login_url = '/authenticate-user/'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        form = WithdrawForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['amount'] >= request.user.wallet.balance:
                context = {
                    'message': "You don't have sufficient balance for this transaction, please fund your account and try again later", 'color': 'red'}
                return render(request, 'services/dashboard.html', context)

            withdrawal = Withdrawal.objects.create(
                **form.cleaned_data, user=request.user)
            withdrawal.save()

            context = {
                'message': 'Your withdrawal request has been placed, you will receive a confirmation email soon. You can monitor updates in transaction history', 'color': 'green'}
            return render(request, 'services/dashboard.html', context)
        else:
            errors = ''
            for field in form:
                if not(field.errors):
                    continue
                error = '<span>{0} '.format(
                    field.label)
                for ferror in field.errors:
                    error += '<br> <span class = "text-base">  {0} </span>'.format(
                        ferror)
                errors += '<br>{0} </span'.format(error)
            context = {'message': errors, 'color': 'red'}
            return render(request, 'services/dashboard.html', context)


# dashboard View
class DashboardView(LoginRequiredMixin, View):
    login_url = '/authenticate-user/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        context = {'bitcoinAddress': '3L3LnvfKMTVZcZJtTR7eLdoMzh4g8n1QyS', 'ethereumAddress': '0x9cbd14f198d4addad022beb882ad069ec2163a3c',
                   'dogecoinAddress': 'D8Kr7nbfG9ykqes5miiq78mfiF6Hf2XnmD', 'litecoinAddress': 'LT4o4VedSQrnCFQus8oPJWMRe2xnNQonUq'}
        return render(request, 'services/dashboard.html', context)


# Verify Code
class VerifyCodeView(View):

    def post(self, request):
        code = request.POST.get('code', '')
        # print("Code is :", code)

        if code == '':
            context = {'message': 'The field is empty', 'color': '#E49B0F'}
            return render(request, 'services/confirmemail.html', context)

        code_object = None
        try:
            code_object = VerificationCode.objects.get(code=code)
        except VerificationCode.DoesNotExist:
            context = {
                'message': 'Incorrect code, please check and try again.', 'color': 'red'}
            return render(request, 'services/confirmemail.html', context)

        saved_user = request.session.get('temporal_saved_data', None)
        if saved_user is None:
            return redirect('/')

        if code_object.email == saved_user['email']:
            fn = saved_user['firstname']
            ln = saved_user['lastname']
            dob = saved_user['dob']
            email = saved_user['email']
            password2 = saved_user['password2']

            user_data = UserData.objects.create(dob=dob)
            user_data.save()
            user = User.objects.create(
                firstname=fn, lastname=ln, email=email, data=user_data)
            user.save()
            user.set_password(password2)
            # print(user.password)
            user.save()
            request.session['temporal_saved_data'] = None
            request.session.flush()

            code_object.delete()

            return redirect(reverse("services:auth_view"))

        else:
            context = {
                'message': 'Incorrect code, please check and try again.', 'color': '#E49B0F'}
            return render(request, 'services/confirmemail.html', context)


# Logout View
class LogoutView(View):
    def get(self, request):
        context = {'message': 'You have been logged out.',
                   'formB': 'hidden', 'formA': 'block'}
        logout(request)
        request.session.flush()
        return render(request, 'services/index.html', context)


# CreateUser View
class CreateUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        context = {'formB': 'block', 'formA': 'hidden', }
        return render(request, 'services/auth.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():

            firstname = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if User.objects.filter(email=email).exists():
                context = {'message': '[ <small>' + email + ' </small>] <br> This email has been taken',
                           'formA': 'hidden', 'formB': 'block'}
                return render(request, 'services/auth.html', context)

            if(password1 and password2) and (password1 == password2):

                saved_user_data = form.cleaned_data.copy()
                saved_user_data['dob'] = request.POST['dob']
                request.session['temporal_saved_data'] = saved_user_data

                # send the code here
                new_code_object = VerificationCode.objects.create(
                    code=generate_unique_code(), email=email)
                new_code_object.save()
                context = {'code': new_code_object.code,
                           'firstname': firstname}

                _message = mail_message(new_code_object.code)

                send_mail(
                    subject='Verification code for  USBEENANCE ACCOUNT [ ' + email + ' ]', from_email='no-reply@usbeenance.com', recipient_list=[email], message="", html_message=_message, fail_silently=False)

                print('\n\nMail Code : ', new_code_object.code)

                return render(request, 'services/confirmemail.html')

            else:
                context = {'message': 'Passwords do not match',
                           'form': form, 'formA': 'hidden', 'formB': 'block'}
                return render(request, 'services/auth.html', context)

        else:
            context = {'form': form, 'formA': 'hidden', 'formB': 'block',
                       'message': 'Invalid form fields', 'color': '#E49B0F'}
            return render(request, 'services/auth.html', context)


class AuthView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        context = {'formA': 'block', 'formB': 'hidden', }

        return render(request, 'services/auth.html', context)

    def post(self, request):

        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                context = {'message': 'Invalid email or password',
                           'color': 'red', 'formB': 'hidden', 'formA': 'block'}
                return render(request, 'services/auth.html', context)
        else:
            context = {'form': form,  'formB': 'hidden',
                       'formA': 'block', 'message': 'Invalid form fields', 'color': 'pink'}
            return render(request, 'services/auth.html', context)
