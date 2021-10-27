# Generated by Django 3.2.6 on 2021-10-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopHeaderWithFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('workingday_start', models.CharField(max_length=100)),
                ('workingday_end', models.CharField(max_length=100)),
                ('Time_start', models.PositiveIntegerField(default=0)),
                ('Time_end', models.PositiveIntegerField(default=0)),
                ('footer_text', models.CharField(max_length=255)),
                ('developed_by', models.CharField(max_length=255)),
                ('facebook_link', models.URLField(max_length=100)),
                ('twitter_link', models.URLField(max_length=100)),
                ('google_plus_link', models.URLField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]