from traceback import print_exception
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Product

from .serializers import (
    PaginationSerializer,
    ProductSerializerViewSet
)



class ProductViewSet(viewsets.ModelViewSet):
    """  """
    serializer_class = ProductSerializerViewSet
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer

   

   
    