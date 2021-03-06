# Generated by Django 2.2 on 2020-09-17 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_merge_20200910_2343'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_auto_20200913_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Коли створено')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Коли змінено')),
                ('sum', models.FloatField(verbose_name='Sum')),
                ('count', models.PositiveSmallIntegerField(default=1, verbose_name='Amount')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_orderitem_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Item name')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_orderitem_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено')),
            ],
            options={
                'verbose_name': 'Order item',
                'verbose_name_plural': 'Order items',
            },
        ),
    ]
