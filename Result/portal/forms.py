from django.db import models
from django import forms
class StudentForm(forms.Form):
    Reg=forms.CharField(max_length=128)
    BirthDate=forms.DateField()
    Math=forms.IntegerField()
    Science=forms.IntegerField()
    Social=forms.IntegerField()