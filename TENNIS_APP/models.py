from platform import mac_ver
from pyexpat import model
from tokenize import Number
from django.db import models
from datetime import datetime


# Create your models here.


class Contact(models.Model):
 name = models.CharField(max_length=150)
 email = models.EmailField(max_length=150)
 mobile_number = models.CharField(max_length=10)
 address = models.TextField()
 
 def __str__(self):
  return self.name
     
     
# Create your models here.
class User(models.Model):
 name = models.CharField(max_length=70)
 email = models.EmailField(max_length=100)
 password = models.CharField(max_length=100)
 
 
 # online Booking
class OnlineBooking(models.Model):
 NUMBER_OF_PLAYER = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
   
]
 
 name =models.CharField(max_length=250)
 date = models.DateField()
 time = models.TimeField(blank=True)
 duration_of_game = models.CharField(max_length=40) 
 number_of_player = models.CharField(max_length=25,choices=NUMBER_OF_PLAYER,default=4)
 
 def __str__(self):
  return self.name
 