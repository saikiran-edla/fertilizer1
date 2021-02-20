from django.db import models

# Create your models here.
class fregistration(models.Model):
    Fname = models.CharField(max_length=10)
    Lname = models.CharField(max_length=10)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    State = models.CharField(max_length=15)
    District = models.CharField(max_length=15)
    Mandal = models.CharField(max_length=15)
    Village = models.CharField(max_length=15)
    Aadhaar = models.IntegerField()
    Passbook = models.CharField(max_length=12)
    Password = models.CharField(max_length=20)
    Repassword = models.CharField(max_length=20)

