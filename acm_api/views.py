from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class GroceryListView(viewsets.ModelViewSet):
    queryset = models.GroceryList.objects.all()
    serializer_class = serializers.GroceryListSerializer

class CheckListView(viewsets.ModelViewSet):
    queryset = models.CheckList.objects.all()
    serializer_class = serializers.CheckListSerializer
