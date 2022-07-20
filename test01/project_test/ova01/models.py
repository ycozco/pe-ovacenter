import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
    member_name = models.CharField(max_length =100)
    member_dni =  models.CharField(max_length = 8)
    member_birthday = models.DateField()
    member_ini = models.DateField()
    member_end = models.DateField()

    def __str__(self) -> str:
        return self.member_name
    
    def was_created_recently(self):
        return self.member_ini >= timezone.now() - datetime.timedelta(days=1)

class Routine(models.Model):
    routine_name = models.CharField(max_length =100)
    routine_description = models.CharField(max_length =100)
    routine_date = models.DateField()
    routine_time = models.TimeField()
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.routine_name


