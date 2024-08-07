# Generated by Django 5.0.6 on 2024-07-04 10:23

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_alter_profiledetails_sate_name'),
        ('project', '0007_alter_product_slugfield'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place_order',
            fields=[
                ('udid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateField(auto_now=True)),
                ('upate_date_by', models.DateField(auto_now_add=True)),
                ('qty', models.PositiveIntegerField(default=1)),
                ('orderdate', models.DateField(auto_now_add=True)),
                ('Stats', models.CharField(choices=[('Delivery', 'Delivery'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Accepted ', 'Accepted'), ('Packed', 'Packed'), ('On the Way', 'On the Way')], default='Pending', max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customerdetails', to='accounts.profiledetails')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allcartproduct', to='project.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mainuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
