from rest_framework import serializers

from acm_api.models import CheckList, GroceryList


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = ['id','text','completed']

# class CheckListField(serializers.ListField):
#     child = CheckListSerializer()

class GroceryListSerializer(serializers.ModelSerializer):
    # items = CheckListSerializer(many=True)
    class Meta:
        model = GroceryList
        fields = "__all__"

    # def create(self, validated_data):
    #     return GroceryList.objects.create(**validated_data)

    # def save(self, *args, **kwargs):
    #     self.revision += 1
    #     return super(GroceryList, self).save()


