from django.db import models
from datetime import datetime

# Create your models here.


class Vacation(models.Model):

    start_date = models.DateField(default=datetime.now,blank=False,null=False)
    end_date = models.DateField(blank=False,Null=False)

    def __str__(self):
        return self.start_date.strftime('%Y,%m,%d')


class Branch(models.Model):

    location = CharField(max_length= 128, blank=False,null=False)
    name = CharField(max_length= 128, blank=False,null=False)

    def __str__(self):
        return self.name