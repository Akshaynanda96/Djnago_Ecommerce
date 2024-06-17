# Generated by Django 5.0.6 on 2024-06-13 09:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_product_product_name_alter_product_slugfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slugField',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='get_slug_source', unique=True),
        ),
    ]
