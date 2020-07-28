from rest_framework import serializers
from . import models


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckList
        fields = ['id','text','completed']

# class CheckListField(serializers.ListField):
#     child = CheckListSerializer()

class GroceryListSerializer(serializers.ModelSerializer):
    items = CheckListSerializer(many=True)
    class Meta:
        model = models.GroceryList
        fields = ['id', 'items']

    def create(self, validated_data):
        return models.GroceryList.objects.create(**validated_data)


