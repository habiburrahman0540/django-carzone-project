# Generated by Django 3.2.6 on 2021-11-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_created_data_car_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
