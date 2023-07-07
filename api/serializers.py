from rest_framework import serializers

from customers.models import Provider


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source="person.name")
    image_url = serializers.ImageField(source="person.image_url")
    rating_score = serializers.DecimalField(
        source="search_score.rating_score", max_digits=2, decimal_places=1
    )
    url = serializers.SerializerMethodField()

    class Meta:
        model = Provider
        fields = ['url', 'name', 'image_url', 'rating_score']

    def get_url(self, obj):
        return 'google.com'
