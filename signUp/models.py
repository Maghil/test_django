from django.db import models

class user_details(models.Model ):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)