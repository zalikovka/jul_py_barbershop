# Generated by Django 2.2 on 2020-08-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_profile', '0019_auto_20200829_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerprofile',
            name='comm_id',
            field=models.CharField(choices=[('Facebook id', 'Facebook id'), ('Instagram id', 'Instagram id'), ('Other id', 'Other id')], default=None, max_length=150),
        ),
    ]
