from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField()
    dob = models.DateField()
    user_bio = models.TextField()


class Interest(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(Member)
