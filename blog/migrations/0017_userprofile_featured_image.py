# Generated by Django 3.2.20 on 2023-09-19 17:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
