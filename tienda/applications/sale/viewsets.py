from datetime import datetime
from django.utils import timezone
#
from rest_framework.decorators import api_view, permission_classes, action
#
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
#
from django.shortcuts import get_object_or_404
#
from applications.product.models import Product
#
from .models import Order, OrderDetail
#
from .serializers import (
SaleProcessSerializer,
SaleReportSerializers,
)


class SalesViewSet(viewsets.ViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = SaleProcessSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if (self.action == 'list') or (self.action == 'retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Order.objects.all()
        serializer = SaleReportSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = SaleReportSerializers(order)
        return Response(serializer.data)

    
    def create(self, request):
        serializer = SaleProcessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sale = Order.objects.create(
            date_order=timezone.now(),
        )
        # recuperamos los products de la sale
        products = serializer.validated_data['products']
        products_ids = [product["pk"] for product in products]
        products_ids = set(products_ids)
        print(products_ids)
        # para cada product regustramos una venta detalle
        sale_details = []
        for product in products:
            if product["pk"] in products_ids:
                print(product["pk"])
                products_ids.remove(product["pk"])
                print(products_ids)
            else:
                continue
            if product['cuantity'] <=0:
                continue
            # recuperamos product
            prod = Product.objects.get(id=product['pk'])
            if prod.stock >= product['cuantity']:
                prod.stock -= product['cuantity']
                prod.save()
                order_detail = OrderDetail(
                    order=sale,
                    product=prod,
                    cuantity=product['cuantity'],
                
                )
                #
                sale_details.append(order_detail)
                print(sale_details)

        OrderDetail.objects.bulk_create(sale_details)
        return Response({'status': 'ok', 'msg':"Successfully created"})

   

    def partial_update(self, request, pk=None):
        data = request.data
        print(data)
        sale = Order.objects.get(
            id=pk,
        )
        # recuperamos los products de la sale
        order_details = data['products']

        # para cada producto regustramos una venta detalle
        sale_details = []
        for detail in order_details:
            # recuperamos order
            prod = Product.objects.get(id=detail['product_id'])
            original_detail = OrderDetail.objects.get(id=detail['id'])
            diferencia = abs(original_detail.cuantity - detail['cuantity'])
            if original_detail.cuantity < detail['cuantity'] and prod.stock < diferencia:                
                continue
            else:
                if original_detail.cuantity < detail['cuantity']:
                    prod.stock -=diferencia
                elif original_detail.cuantity > detail['cuantity']:
                    prod.stock +=diferencia
                prod.save()
                order_detail = OrderDetail(
                        id=detail['id'],
                        order=sale,
                        product=prod,
                        cuantity=detail['cuantity'],
                    )
                    #
                sale_details.append(order_detail)


        OrderDetail.objects.bulk_update(sale_details, fields = ['order','product','cuantity'])
        return Response({'status': 'ok', 'msg':"Successfully saved"})
    

    def destroy(self, request, pk=None):
        order = Order.objects.get(id=pk)  
        details = OrderDetail.objects.select_related().filter(order = pk)      
        for detail in details:
            prod = Product.objects.get(id=detail.product_id)
            prod.stock += detail.cuantity
            prod.save()
        order.delete()
    
        return Response({'status': 'ok', 'msg':"Successfully deleted"})
