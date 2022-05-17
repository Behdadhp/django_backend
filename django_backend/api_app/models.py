from django.db import models
from datetime import datetime

# Create your models here.


class Vacation(models.Model):

    start_date = models.DateField(default=datetime.now,blank=False,null=False)
    end_date = models.DateField(blank=False,null=False)

    def __str__(self):
        return self.start_date.strftime('%Y,%m,%d')


class Branch(models.Model):

    location = models.CharField(max_length= 128, blank=False,null=False)
    name = models.CharField(max_length= 128, blank=False,null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):

    username = models.CharField(max_length=64,blank=False,null=False)
    first_name = models.CharField(max_length=64,blank=False,null=False)
    last_name = models.CharField(max_length=64,blank=False,null=False)
    email = models.EmailField(max_length=64,blank=False,null=False)
    related_branch = models.ForeignKey(Branch,related_name='branch',on_delete=models.CASCADE)

    def __str__(self):
        return self.username