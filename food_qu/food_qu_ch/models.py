from django.db import models

# Create your models here.




class list_name(models.Model):
    list_id =models.IntegerField(primary_key=True)
    list_name = models.CharField(max_length=100)
    list_location = models.CharField(max_length=400)
    list_quality_expiry = models.DateTimeField()
    list_price = models.FloatField(default=0)
    list_rating = models.FloatField(default=3.0)
    list_email = models.EmailField()

class ver(models.Model):
    list_id =models.IntegerField(primary_key=True)
    list_name = models.CharField(max_length=100)
    list_location = models.CharField(max_length=400)
    list_price = models.FloatField(default=0)
    list_email = models.EmailField()


    
class log(models.Model):
    name=models.CharField(unique=True,max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateField(auto_now_add=True)

class logins(models.Model):
    name=models.CharField(unique=True,max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateField(auto_now_add=True)