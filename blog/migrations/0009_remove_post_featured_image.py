# Generated by Django 3.2.20 on 2023-09-08 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20230908_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
    ]
