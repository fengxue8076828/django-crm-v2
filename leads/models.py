from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_organizer=models.BooleanField(default=True)
    is_agent=models.BooleanField(default=False)

class Organizer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Agent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    organizer=models.ForeignKey(Organizer,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Category(models.Model):
    choice=[
        ("new","new"),
        ("converted","converted"),
        ("unconverted","unconverted")
    ]
    name=models.CharField(max_length=20,choices=choice)

    def __str__(self):
        return self.name

class Lead(models.Model):
    agent=models.ForeignKey(Agent,null=True,blank=True,on_delete=models.SET_NULL)
    organizer=models.ForeignKey(Organizer,null=True,blank=True,on_delete=models.SET_NULL)
    category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.CharField(max_length=100)
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    

