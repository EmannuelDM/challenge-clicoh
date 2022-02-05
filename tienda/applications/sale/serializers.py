#
from rest_framework import serializers
#
from .models import Order, OrderDetail


class ProductDetailSerializers(serializers.Serializer):    
    pk = serializers.IntegerField()
    cuantity = serializers.IntegerField()


class SaleProcessSerializer(serializers.Serializer):
    products = ProductDetailSerializers(many=True)



class SaleReportSerializers(serializers.ModelSerializer):
    """ serializdor para ver las ventas en detalle """

    products = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    usd_total = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = (
            'id',
            'date_order',
            'products',
            'total',
            'usd_total'
        )
    
    def get_products(self, obj):
        queryset = OrderDetail.objects.products_per_order(obj.id)
        return OrderDetailsSerializer(queryset, many=True).data
    def get_total(self, obj):
        queryset = OrderDetail.objects.products_per_order(obj.id)
        return Order.objects.get_total(queryset)
    def get_usd_total(self, obj):
        queryset = OrderDetail.objects.products_per_order(obj.id)
        return Order.objects.get_total_usd(queryset)

 

class OrderDetailsSerializer(serializers.ModelSerializer):
    """ serializdor para ver las ventas en detalle """
    product = serializers.CharField(source='product.name')
    product_id = serializers.IntegerField(source='product.id')
    class Meta:
        model = OrderDetail
        fields = (
            'id',
            'order',
            'product',
            'product_id',
            'cuantity'
        )
