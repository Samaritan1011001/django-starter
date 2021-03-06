from rest_framework import serializers
from acm_api.models import CheckList, GroceryList


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = ['id','text','completed']


class GroceryListSerializer(serializers.ModelSerializer):
    checklist_items = CheckListSerializer(many=True)
    class Meta:
        model = GroceryList
        fields = ["id", "name", "checklist_items"]

    def create(self, validated_data):
        print("validated_data -> ",validated_data)
        return GroceryList.objects.create(**validated_data)


