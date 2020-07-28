from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializers
from rest_framework import generics



class GroceryListView(generics.ListCreateAPIView):
    queryset = models.GroceryList.objects.all()
    serializer_class = serializers.GroceryListSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        print(request)
        queryset = self.get_queryset()
        serializer = serializers.GroceryListSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CheckListView(viewsets.ModelViewSet):
    queryset = models.CheckList.objects.all()
    serializer_class = serializers.CheckListSerializer


