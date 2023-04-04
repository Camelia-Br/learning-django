from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from customers.models import Provider
from api.serializers import *


class ProviderListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
