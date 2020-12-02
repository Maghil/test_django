from django import forms

class signUpForm(forms.Form):
    username = forms.CharField(label='user name', max_length=50)
    email = forms.CharField(label='email', max_length=50)
    password = forms.CharField(label='password', max_length=50)
    cnfrmpassword = forms.CharField(label='cnfrmpassword', max_length=50)

class loginInfo(forms.Form):
    username= forms.CharField(label='username' ,max_length=25)
    password=forms.CharField(label='password' ,max_length=30)