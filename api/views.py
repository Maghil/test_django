from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serailizers import *
# from .serailizers import SignupSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'signup': '/signUp',
        'login': '/login',
    }
    return Response(api_urls)

@api_view(['POST'])
def signUp(request):

    # a=SignupSerializer()
    return HttpResponse(request)

@api_view(['GET'])
def login(request):
    return HttpResponse("login")

