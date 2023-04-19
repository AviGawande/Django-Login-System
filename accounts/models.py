from django.db import models

class Accounts(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)
    
