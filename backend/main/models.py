from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    pic_loc = models.CharField(max_length=150)


class Teacher(models.Model):
    member = models.ForeignKey(User)
    good_at = models.ManyToManyField(Category)


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    posted_on = models.DateTimeField()
    start_from = models.DateField()
    end_on = models.DateField()
    deadline = models.DateTimeField()
    hosted_by = models.ManyToManyField(Teacher)
    categories = models.ManyToManyField(Category)
    click_counter = models.IntegerField(default=0)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField()
    dob = models.DateField()
    user_bio = models.TextField()
    interested_in = models.ManyToManyField(Category)
    lessons_joint = models.ManyToManyField(Lesson)


class Wish(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    posted_by = models.ForeignKey(User)
    posted_on = models.DateTimeField()
    click_counter = models.IntegerField(default=0)
