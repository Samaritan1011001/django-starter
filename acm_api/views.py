from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status, generics, request
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from acm_api.models import CheckList
from . import models
from . import serializers


# Mixin that allows to create multiple objects from lists.
class CreateListModelMixin(object):
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)

class GroceryListView(generics.ListCreateAPIView):
    queryset = models.GroceryList.objects.all()
    serializer_class = serializers.GroceryListSerializer

class GListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.GroceryList.objects.all()
    serializer_class = serializers.GroceryListSerializer

class CheckListView(generics.ListAPIView):
    model = CheckList
    # queryset = models.CheckList.objects.filter()
    serializer_class = serializers.CheckListSerializer

    # def get_serializer_class(self, *args, **kwargs):
    #     return serializers.CheckListSerializer
    #
    # def get_serializer(self, *args, **kwargs):
    #     print("args -> ",args)
    #     print("kwargs -> ",kwargs)
    #     return self.get_serializer_class(self)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.CheckList.objects.filter(items_id= pk)


    def perform_create(self, serializer: serializers.CheckListSerializer):
        # print("called ->", serializer)
        glist, created = models.GroceryList.objects.get_or_create(id=self.kwargs['pk'])
        checklist = CheckList(**serializer.validated_data)
        glist.checklist_items.add(checklist,bulk=False)
        checklist.save()



