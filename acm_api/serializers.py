from rest_framework import serializers
from . import models


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckList
        fields = ['id','text','completed']


class GroceryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroceryList
        fields = ['id','item']