from django.db import models
from rest_framework import serializers

class GroceryList(models.Model):
    name = models.CharField(max_length=50, default="")

class CheckList(models.Model):
    text = models.CharField(max_length=50,default="")
    completed = models.BooleanField(default=False)
    items = models.ForeignKey(GroceryList, related_name='checklist_items', on_delete=models.CASCADE, default="")

    def __str__(self):
        return '%s: %d' % (self.text, self.completed)

