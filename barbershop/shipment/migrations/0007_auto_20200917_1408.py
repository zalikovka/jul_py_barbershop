# Generated by Django 2.2 on 2020-09-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0006_auto_20200917_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='buyer_name',
            field=models.CharField(max_length=50),
        ),
    ]