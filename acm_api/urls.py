from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.generics import ListCreateAPIView, CreateAPIView

from acm_api.views import CheckListView, GroceryListView
from . import views
from . import models
from . import serializers

router = routers.DefaultRouter()
# router.register(r'glists',  GroceryListView, basename="g-lists")
# router.register(r'checklists', views.CheckListView,basename="check-lists")

urlpatterns = [
    path(r'', include(router.urls)),
    # url(r'glists', GroceryListView.as_view()),
    # url(r'checklists', CheckListView.as_view())
    # url(r'glists', CreateAPIView.as_view(queryset=models.GroceryList.objects.all(), serializer_class=serializers.GroceryListSerializer))
    # url(r'checklists', CheckListView.as_view(queryset=models.CheckList.objects.all(), serializer_class=serializers.CheckListSerializer))

    path('glists/<int:pk>/checklist/', views.CheckListView.as_view()),
    path('glists/', views.GroceryListView.as_view()),
    path('glists/<int:pk>/', views.GListDetail.as_view()),
]