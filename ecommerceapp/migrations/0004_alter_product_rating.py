# Generated by Django 5.0.6 on 2024-09-26 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=1),
        ),
    ]
