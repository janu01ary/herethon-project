from django.db import models

# Create your models here.
class Email(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)

class Result(models.Model):
    date = models.DateField()
    score = models.IntegerField()
    division = models.CharField(max_length=10)
