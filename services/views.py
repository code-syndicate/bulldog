import uuid
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login
from users.models import User, UserData, VerificationCode


def generate_unique_code():
    code = uuid.uuid4().clock_seq
    if VerificationCode.objects.filter(code=code).count() > 1:
        return generate_unique_code()

    return code

    # Index View


class IndexView(View):
    def get(self, request):
        context = {'formB': 'hidden', 'formA': 'block'}
        return render(request, 'services/index.html', context)


# dashboard View
class DashboardView(View):
    def get(self, request):
        return render(request, 'services/dashboard.html')


# Verify Code
class VerifyCodeView(View):
    def post(self, request):
        code = request.POST.get('code', '')

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
            user.set_password(password2)
            user.save()
            request.session['temporal_saved_data'] = None
            request.session.flush()

            code_object.delete()

            return redirect(reverse("services:auth_view"))

        else:
            context = {
                'message': 'Incorrect code, please check and try again.', 'color': '#E49B0F'}
            return render(request, 'services/confirmemail.html', context)


# CreateUser View
class CreateUserView(View):
    def get(self, request):
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
                mail_message = str(render(
                    request, 'services/verifymailtemplate.html', context).content)

                print('\n\nMail Code : ', new_code_object.code)

                send_mail(
                    subject='Verification code for  USBEENANCE ACCOUNT [ ' + email + ' ]', from_email='truecitizenbank@gmail.com', recipient_list=[email, ], message=mail_message, fail_silently=True)

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
