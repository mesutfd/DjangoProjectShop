# Generated by Django 4.1.5 on 2023-01-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products/', verbose_name='تصویر محصول'),
        ),
    ]
