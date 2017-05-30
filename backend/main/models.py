from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    pic_loc = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    member = models.ForeignKey(User)
    good_at = models.ManyToManyField(Category)

    def __str__(self):
        return self.member


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    posted_on = models.DateTimeField()
    start_from = models.DateField()
    end_on = models.DateField()
    deadline = models.DateTimeField()
    hosted_by = models.ManyToManyField(User)
    categories = models.ManyToManyField(Category)
    click_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField()
    dob = models.DateField()
    user_bio = models.TextField()
    interested_in = models.ManyToManyField(Category)
    lessons_joint = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.user


class Wish(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    posted_by = models.ForeignKey(User)
    posted_on = models.DateTimeField()
    click_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title






# for i in range(1,6):
#     l = Lesson.objects.create(name="art_test"+str(i).zfill(2),
#         description="art_test"+str(i).zfill(2)+"desc",
#         price=100.0,
#         posted_on=timezone.now(),
#         start_from=datetime(2017,5,20),
#         end_on=datetime(2017,5,25),
#         deadline=datetime(2017,5,15),
#     )
#     l.hosted_by.set([User.objects.get(username='eason')])
#     l.categories.set([Category.objects.get(name='烹飪')])
#     l.save()
