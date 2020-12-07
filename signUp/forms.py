from django import forms

class signUpForm(forms.Form):
    user_name = forms.CharField(label='username', max_length=20)
    email = forms.CharField(label='email', max_length=40)
    password = forms.CharField(label='password', max_length=20)
    cnfrm_password = forms.CharField(label='confirmpassword', max_length=20)

class loginInfo(forms.Form): 
    user_name= forms.CharField(label='username' ,max_length=20)
    password=forms.CharField(label='password' ,max_length=20)