from django.db import models


class ProductManager(models.Manager):

  
    def products_con_stock(self):
        # lista products con stock mayor a cero

        return self.filter(
            stock__gt=0,
        ).order_by('-num_orders')
    

    def filtrar_products(self, **filtros):
        return self.filter(
            name__icontains=filtros['name']
        )
            
            