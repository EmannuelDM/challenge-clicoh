from django.db import models

#
class OrderDetailManager(models.Manager):
    
    def products_per_order(self, sale_id):
        query = self.filter(
            order__id=sale_id
        ).order_by('cuantity', 'product__name')
        return query