from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status, generics, request
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

class CheckListView(generics.ListCreateAPIView):
    model = CheckList
    queryset = models.CheckList.objects.all()
    serializer_class = serializers.CheckListSerializer

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     print(request)
    #     queryset = self.get_queryset()
    #     serializer = serializers.CheckListSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def get(self):
    #     return self.get_object()
#
# @csrf_exempt
# def CheckListView(request):
#     model = CheckList
#     queryset = models.CheckList.objects.all()
#     serializer_class = serializers.CheckListSerializer
#
#     """
#         List all code snippets, or create a new snippet.
#         """
#     if request.method == 'GET':
#         snippets = CheckList.objects.all()
#         serializer = serializers.CheckListSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = serializers.CheckListSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#



