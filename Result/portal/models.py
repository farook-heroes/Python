from django.db import models

# Create your models here.
class Student(models.Model):
    Reg=models.CharField(max_length=128,blank=False,primary_key=True)
    BirthDate=models.DateField(blank=False)
    Math=models.IntegerField(default=0)
    Science=models.IntegerField(default=0)
    Social=models.IntegerField(default=0)