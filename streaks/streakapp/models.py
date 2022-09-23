from django.db import models

# Create your models here.

class Question(models.Model):
    lc_question_id = models.IntegerField()
    date = models.DateTimeField()

class User(models.Model):
    lc_username = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    date_joined = models.DateTimeField()