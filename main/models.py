from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

class Question(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)