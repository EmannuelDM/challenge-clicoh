from rest_framework import serializers, pagination

from .models import Product


# Para paginacion
class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 50


class ProductSerializerViewSet(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            '__all__'
        )