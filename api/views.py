from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.db.models import Q
import math
from api.serializers import *
from customers.models import Provider


class ProviderListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        average_rating_min = float(self.request.query_params.get("average_rating_min", 1.5))
        average_rating_max = float(self.request.query_params.get("average_rating_max", 4.3))

        if average_rating_min > average_rating_max:
            raise ValueError("The average_rating_min parameter should be smaller than average_rating_max")

        if average_rating_min < 0 or average_rating_max > 5:
            raise ValueError(
                "The average_rating_min parameter should be greater than 0 and average_rating_max parameter should be smaller than 5"
            )

        queryset = queryset.filter(
            Q(search_score__rating_score__gte=average_rating_min)
            & Q(search_score__rating_score__lte=average_rating_max)
        )
        return queryset
