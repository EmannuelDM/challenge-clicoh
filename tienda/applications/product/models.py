from django.db import models
from django.conf import settings


from model_utils.models import TimeStampedModel

from .managers import ProductManager

class Product(TimeStampedModel):
    """
    Modelo que representa un Producto
    """

    #TODO los id tiene que ser string con uuid?????

    name = models.CharField(
        'name', 
        max_length=100
    )
   
    price = models.FloatField(
        'price',
    )
    stock = models.PositiveIntegerField('Stock', default=0)

    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)