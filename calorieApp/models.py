from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Custom_user(AbstractUser):
    GENDER={
        ('male','Male'),
        ('female','Female'),
    }
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDER, max_length=100, null=True)
    height =models.CharField(max_length=100, null=True)
    weight =models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='static/media/user_pic', null=True)


class calorieInfo(models.Model):
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE, null=True)
    result = models.CharField(max_length=100, null=True)


class foods(models.Model):
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    consume = models.IntegerField(null=True)
    date = models.DateField(null=True)