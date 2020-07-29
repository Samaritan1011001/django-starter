from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializers
from rest_framework import generics


# Mixin that allows to create multiple objects from lists.
class CreateListModelMixin(list):
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)

class GroceryListView(CreateListModelMixin, generics.CreateAPIView):
    queryset = models.GroceryList.objects.all()
    serializer_class = serializers.GroceryListSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        print(request)
        queryset = self.get_queryset()
        serializer = serializers.GroceryListSerializer(queryset, many=True)
        return Response(serializer.data)
    #
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def perform_create(self, serializer):
    #     serializer.save()
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


# class CheckListView(viewsets.ModelViewSet):
#     queryset = models.CheckList.objects.all()
#     serializer_class = serializers.CheckListSerializer

class CheckListView(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = models.CheckList.objects.all()
    serializer_class = serializers.CheckListSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        print(request)
        queryset = self.get_queryset()
        serializer = serializers.CheckListSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self):
        return self.get_object()


