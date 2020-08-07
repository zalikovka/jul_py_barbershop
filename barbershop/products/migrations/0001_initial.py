# Generated by Django 2.2.14 on 2020-08-07 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.CharField(max_length=100, verbose_name='Products')),
                ('prices', models.PositiveIntegerField(default=0, help_text='indicate the cost', verbose_name='Prices')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
