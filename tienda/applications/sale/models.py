from django.db import models
from django.conf import settings

#
from model_utils.models import TimeStampedModel

# 
from applications.product.models import Product

#
from .managers import OrderDetailManager, OrderManager


class Order(TimeStampedModel):
    """
    Modelo que representa a una Sale Global
    """
    #TODO el id es un string???

    date_order = models.DateTimeField(
        'Sale Date',
        blank=True,
        null=True
    )
   
    objects = OrderManager()

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'sales'

    def __str__(self):
        return 'Nº [' + str(self.id) + '] - ' + str(self.date_order)



class OrderDetail(TimeStampedModel):
    """
    Model of the sale detail
    """

    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        verbose_name='Order Code'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    cuantity = models.PositiveIntegerField('Cuantity')
    
    objects = OrderDetailManager()

    class Meta:
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'

    def __str__(self):
        return str(self.order.id) + ' - ' + str(self.product.name)
