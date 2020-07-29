from django.db import models
from rest_framework import serializers



class CheckList(models.Model):
    text = models.CharField(max_length=50,default="")
    completed = models.BooleanField(default=False)
    # items = models.ForeignKey(GroceryList,on_delete=models.CASCADE,default="")
    # id = models.AutoField(primary_key=True)

class GroceryList(models.Model):
    # items = models.CharField(default="",max_length=50)
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50, default="")
    completed = models.BooleanField(default=False)


