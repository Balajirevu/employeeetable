from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=30)
class Employee(models.Model):
    Fullname=models.CharField(max_length=100)
    Empcode=models.IntegerField()
    Mobile=models.IntegerField()
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
