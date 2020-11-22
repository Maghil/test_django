from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import loginForm

def login(request):
    form = loginForm(request.POST)
    return render(request, 'testform.html', {'form': form})

def home(request):
    if request.method == 'POST':
        if request.POST.get('first_name')=="maghil" and request.POST.get("last_name")=="maghil":
            return HttpResponse("<h1>hello "+request.POST.get('first_name')+"</h1>")
        else:
            return HttpResponse("<h1>hello hacker </h1>")