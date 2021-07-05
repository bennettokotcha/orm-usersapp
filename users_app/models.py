from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=75)
    email_address = models.TextField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.

