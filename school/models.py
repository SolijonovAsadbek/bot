from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=256)
