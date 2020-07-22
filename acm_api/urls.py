
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register("grocerylists", views.GroceryListView)
router.register("checklists", views.CheckListView)

urlpatterns = [
    path('', include(router.urls))
]