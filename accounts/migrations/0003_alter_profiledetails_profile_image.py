# Generated by Django 5.0.6 on 2024-06-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profiledetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_picture'),
        ),
    ]
