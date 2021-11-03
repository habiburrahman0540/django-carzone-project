# Generated by Django 3.2.6 on 2021-11-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_video_title', models.CharField(max_length=255)),
                ('service_video_description', models.TextField()),
                ('service_video_link', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
