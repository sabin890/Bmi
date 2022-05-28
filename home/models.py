from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bmi(models.Model):
    hight=models.FloatField()
    weight=models.FloatField()
    age=models.IntegerField()
    result=models.FloatField()
    suggest=models.TextField(max_length=300, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    