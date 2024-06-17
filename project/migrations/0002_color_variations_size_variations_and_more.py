# Generated by Django 5.0.6 on 2024-06-07 07:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='color_variations',
            fields=[
                ('udid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateField(auto_now=True)),
                ('upate_date_by', models.DateField(auto_now_add=True)),
                ('color_name', models.CharField(max_length=100)),
                ('color_price', models.ImageField(default=0, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Size_variations',
            fields=[
                ('udid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateField(auto_now=True)),
                ('upate_date_by', models.DateField(auto_now_add=True)),
                ('Size_name', models.CharField(max_length=100)),
                ('Size_price', models.ImageField(default=0, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_Brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_artical',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=models.ManyToManyField(blank=True, null=True, to='project.color_variations'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_Size',
            field=models.ManyToManyField(blank=True, null=True, to='project.size_variations'),
        ),
    ]
