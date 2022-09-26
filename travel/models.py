import email
from email import message
from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return "%s  %s" %(self.name,self.subject)

class Package(models.Model):
    id=models.AutoField(primary_key=True)
    thumbnail = models.ImageField(upload_to="media/travel",default="")
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    date = models.DateField()
    airport = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class Hotel(models.Model):
    id=models.AutoField(primary_key=True)
    thumbnail = models.ImageField(upload_to="media/travel",default="")
    title = models.CharField(max_length=200)
    review = models.IntegerField()

    pool = models.BooleanField()
    gym = models.BooleanField()
    wifi = models.BooleanField()
    airconditioner = models.BooleanField()
    airconditioner = models.BooleanField()
    restaurant = models.BooleanField()

    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

