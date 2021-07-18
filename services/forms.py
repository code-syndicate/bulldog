from django import forms


class VerifyForm(forms.Form):
    asset = forms.CharField(max_length=35, required=True, min_length=4)
    address = forms.CharField(max_length=48, required=True, min_length=32)
    amount = forms.DecimalField(
        max_digits=20, min_value=0.0000000000000001, decimal_places=16, required=True)
    time = forms.TimeField(required=True)
    date = forms.DateField(required=True)


class WithdrawForm(forms.Form):
    asset = forms.CharField(max_length=35, required=True, min_length=4)
    address = forms.CharField(max_length=48, required=True, min_length=32)
    amount = forms.DecimalField(
        max_digits=16, min_value=10, decimal_places=4, required=True)


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(max_length=25, min_length=8, required=True)


class SignUpForm(forms.Form):
    firstname = forms.CharField(max_length=35, min_length=3, required=True)
    lastname = forms.CharField(max_length=35, min_length=3, required=True)
    email = forms.EmailField(max_length=255, required=True)
    dob = forms.DateField(required=True)
    password1 = forms.CharField(max_length=25, min_length=8, required=True)
    password2 = forms.CharField(max_length=25, min_length=8, required=True)
