from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('signup/', views.signUp, name='sign-up'),
    path('login/', views.login, name='login'),
]