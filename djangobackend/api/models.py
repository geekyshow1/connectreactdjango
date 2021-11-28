from django.db import models

# Create your models here.
class Student(models.Model):
  stuname = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
