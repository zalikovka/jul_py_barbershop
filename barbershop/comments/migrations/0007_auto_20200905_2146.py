# Generated by Django 2.2 on 2020-09-05 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_auto_20200905_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentitem',
            name='comment_ptr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_item', to='comments.Comment'),
        ),
    ]
