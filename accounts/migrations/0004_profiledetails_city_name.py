# Generated by Django 5.0.6 on 2024-06-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profiledetails_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='city_name',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
    ]
