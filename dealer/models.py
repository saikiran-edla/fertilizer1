from django.db import models

# Create your models here.
class sregistration(models.Model):
    Name = models.CharField(max_length=15)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
class Product(models.Model): 
    Email = models.EmailField()
    Pname = models.CharField(max_length=15)
    Pprice = models.IntegerField()
    Pdesc = models.TextField()
    Pimage = models.ImageField(upload_to='images')