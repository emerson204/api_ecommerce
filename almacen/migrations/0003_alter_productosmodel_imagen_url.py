# Generated by Django 5.1.1 on 2024-09-19 04:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_productosmodel_imagen_url_full_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosmodel',
            name='imagen_url',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
