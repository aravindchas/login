from django.db import models

# Create your models here.
class Logindetails(models.Model):
    username=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=30)
