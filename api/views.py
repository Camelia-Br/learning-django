from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.db.models import Q

from api.serializers import *
from customers.models import Provider


class ProviderListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProviderSerializer

    def get_queryset(self):
        average_rating_min = self.request.query_params.get("average_rating_min", 3)
        average_rating_max = self.request.query_params.get("average_rating_max", 5)

        queryset = Provider.objects.all()
        queryset= queryset.filter(Q(search_score__rating_score__gte=average_rating_min), search_score__rating_score__lte=average_rating_max)
        return queryset
      


