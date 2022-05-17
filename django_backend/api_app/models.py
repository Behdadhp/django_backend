from django.db import models
from datetime import datetime

# Create your models here.


class Vacation(models.Model):

    start_date = models.DateField(default=datetime.now,blank=False,Null=False)
    end_date = models.DateField(blank=False,Null=False)

    def __str__(self):
        return self.start_date.strftime('%Y,%m,%d')

