# Generated by Django 3.2.20 on 2023-09-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20230920_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]