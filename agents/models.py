from django.db import models
from django.conf import settings
from django.conf import settings
User=settings.AUTH_USER_MODEL

class Agent(models.Model):
    nume=models.CharField(max_length=140)
    image=models.ImageField(upload_to='images/')
class Mock(models.Model):
    user=models.ForeignKey(User, on_delete='SET_NULL')
    nume=models.CharField(max_length=140)
    position=models.CharField(max_length=140,default="CNN Agent")
    description=models.TextField(max_length=1500)
    image = models.ImageField(upload_to='static/',null=True)
    rating=models.PositiveSmallIntegerField()
    mature=models.BooleanField(default=False)
    pricepergb=models.IntegerField(null=True)
    earned=models.IntegerField(null=True)
    developer=models.CharField(max_length=80, default="ATN")

    def __str__(self):
        return self.nume

class Category(models.Model):
    nume=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    icon=models.CharField(max_length=100)
    def __str__(self):
        return self.nume

class Product(models.Model):
    owner=models.ForeignKey(User, on_delete='SET_NULL')
    nume=models.CharField(max_length=100)
    category=Category;
    def __str__(self):
        return self.nume
