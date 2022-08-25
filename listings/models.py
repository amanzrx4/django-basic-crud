from cgi import print_exception
from configparser import MAX_INTERPOLATION_DEPTH
from ctypes import addressof
from logging.handlers import RotatingFileHandler
from turtle import title
from django.db import models

# Create your models here.
class Listing(models.Model):
  title = models.CharField(max_length=150)
  price = models.IntegerField()
  num_bedrooms = models.IntegerField()
  num_bathrooms = models.IntegerField()
  square_footage = models.IntegerField()
  address = models.CharField(max_length=100)
  image = models.ImageField()
  
  def __str__(self):
    return self.title
