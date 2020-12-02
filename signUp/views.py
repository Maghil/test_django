from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import signUpForm, loginInfo

def signUp(request):
    form = signUpForm(request.POST)
    return render(request, 'signup.html', {'form': form})

def login(request):
    form=loginInfo(request.POST)
    return render(request,'login.html',{'form':form})

def home(request):
    if request.method == 'POST':
        if request.POST.get('username')=="maghil" and request.POST.get("password")=="maghil":
            return HttpResponse("<h1>hello "+request.POST.get('username')+"</h1><br><br><a href='../login'>LogOut</a>")
        elif request.POST.get('username')=="" and request.POST.get("password")=="":
            return redirect('/login')
        else:
            return HttpResponse("<h1>hello hacker </h1><br><a href='../login'>Back To Login Page</a>")