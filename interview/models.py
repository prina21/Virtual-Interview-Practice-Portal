from enum import unique
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    class Meta:
        unique_together = ['choice', 'filename']
    INTERVIEW_CHOICE = (('experienced','Experienced'),('fresher','Fresher'))
    choice = models.CharField(max_length=80,choices = INTERVIEW_CHOICE)
    filename = models.IntegerField()
    question = models.CharField(max_length=250)

