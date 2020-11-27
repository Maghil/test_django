from django import forms

class signUpForm(forms.Form):
    user_name = forms.CharField(label='user name', max_length=50)
    email = forms.CharField(label='email', max_length=50)
    password = forms.CharField(label='password', max_length=50)