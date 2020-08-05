from rest_framework import serializers

from acm_api.models import CheckList, GroceryList


class CheckListSerializer(serializers.ModelSerializer):

    class Meta:
        # many = True
        model = CheckList
        fields = ['id','text','completed']


class GroceryListSerializer(serializers.ModelSerializer):
    checklist_items = CheckListSerializer(many=True)
    class Meta:
        model = GroceryList
        fields = ["id", "name", "checklist_items"]

    def create(self, validated_data):
        return GroceryList.objects.create(**validated_data)
    #
    # def save(self, *args, **kwargs):
    #     self.revision += 1
    #     return super(GroceryList, self).save()

