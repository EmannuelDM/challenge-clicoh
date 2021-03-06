# Generated by Django 3.0.5 on 2022-02-05 03:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date_order', models.DateTimeField(blank=True, null=True, verbose_name='Sale Date')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'sales',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('cuantity', models.PositiveIntegerField(verbose_name='Cuantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Order', verbose_name='Order Code')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'Order Detail',
                'verbose_name_plural': 'Order Details',
            },
        ),
    ]
