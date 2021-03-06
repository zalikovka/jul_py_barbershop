# Generated by Django 2.2 on 2020-08-20 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0004_auto_20200819_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_cart_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено'),
        ),
        migrations.AddField(
            model_name='cart',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Коли створено'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_cart_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено'),
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Коли змінено'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_cartitem_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Коли створено'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_cartitem_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Коли змінено'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
