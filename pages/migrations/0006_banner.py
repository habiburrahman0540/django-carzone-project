# Generated by Django 3.2.6 on 2021-11-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_teamsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title_1', models.CharField(max_length=255)),
                ('banner_title_2', models.CharField(max_length=255)),
                ('banner_title_2_extra', models.CharField(max_length=255)),
                ('banner_image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
