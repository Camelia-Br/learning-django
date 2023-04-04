from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from customers.models import Provider
from api.serializers import *


class ProviderListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Provider.objects.all()
        serializer = ProviderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Provider.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProviderSerializer(user)
        return Response(serializer.data)
