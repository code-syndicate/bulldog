from django import forms


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
