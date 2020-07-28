from django.db import models
from rest_framework import serializers


class GroceryList(models.Model):
    # items = models.Field(serialize=serializers.ListField, default=[])
    id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        self.revision += 1
        return super(GroceryList, self).save(*args, **kwargs)

class CheckList(models.Model):
    text = models.CharField(max_length=50,default="")
    completed = models.BooleanField(default=False)
    # g_list = models.ForeignKey(GroceryList,on_delete=models.CASCADE,default="")

    # id = models.AutoField(primary_key=True)

