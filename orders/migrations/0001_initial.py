# Generated by Django 3.2 on 2022-09-12 19:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=orders.models.generator, max_length=8, verbose_name='Order CODE')),
                ('order_status', models.CharField(choices=[('Recieved', 'Recieved'), ('Processed', 'Processed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=20, verbose_name='Order Status')),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Order Time')),
                ('delivery_time', models.DateTimeField(blank=True, null=True, verbose_name='Delivery Time')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
                ('price', models.FloatField(verbose_name='Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Detail_Order', to='orders.order', verbose_name='Order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='OrderDetail_product')),
            ],
        ),
    ]
