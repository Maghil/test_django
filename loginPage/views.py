from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import loginForm

def index(request):
    form = loginForm(request.POST)

    return render(request, 'testform.html', {'form': form})

def main(request):
    if request.method == 'POST': 
        return HttpResponse("<h1>hello "+request.POST.get('first_name')+"</h1>")