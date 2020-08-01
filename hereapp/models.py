from django.db import models

# Create your models here.
class Email(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)