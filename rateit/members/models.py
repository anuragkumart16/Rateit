
from django.db import models

class UserRegistration(models.Model):
    date = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
