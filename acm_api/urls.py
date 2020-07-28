from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.generics import ListCreateAPIView

from . import views
from . import models
from . import serializers

router = routers.DefaultRouter()
# router.register(r'glists',  ListCreateAPIView.as_view(queryset=models.GroceryList.objects.all(), serializer_class=serializers.GroceryListSerializer), name='grocery-list')
router.register(r'checklists', views.CheckListView)

urlpatterns = [
    path(r'', include(router.urls)),
    url(r'glists', ListCreateAPIView.as_view(queryset=models.GroceryList.objects.all(), serializer_class=serializers.GroceryListSerializer), name='grocery-list')
]