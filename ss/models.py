# models.py
from django.db import models

class color(models.Model):
    color_name =models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.color_name

class Person(models.Model):
    color = models.ForeignKey(color, null=True, blank= True, on_delete=models.CASCADE, related_name="color")
    name = models.CharField(max_length=100)
    age = models.IntegerField()

