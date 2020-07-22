
from django.db import models
from rest_framework.fields import Field


class CheckList(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)


class GroceryList(models.Model):
    item = Field(source="CheckList")
