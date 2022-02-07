from django.db import models
from ..product.models import Product
import requests

#
class OrderDetailManager(models.Manager):
    
    def products_per_order(self, sale_id):
        query = self.filter(
            order__id=sale_id
        ).order_by('cuantity', 'product__name')
        return query

class OrderManager(models.Manager):
    def get_total(self, details):
        try:
            total = 0
            for detail in details:
                prod = Product.objects.get(id=detail.product_id)
                total += prod.price
            return total
        except Exception as e:
            return "error"

    def get_total_usd(self, details):
        try:
            response = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
            if response.status_code == 200:
                buy_price = response.json()[1]['casa']['venta']
                if buy_price is not None:
                    buy_price = float(buy_price.replace(',','.'))
                    total = 0
                    for detail in details:
                        prod = Product.objects.get(id=detail.product_id)
                        total += prod.price
                    return round(total / buy_price ,2)
            return "No disponible"
        except Exception as e:
            return "error"
