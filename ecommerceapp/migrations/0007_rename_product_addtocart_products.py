# Generated by Django 5.0.6 on 2024-09-30 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0006_alter_orderplaced_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocart',
            old_name='product',
            new_name='products',
        ),
    ]
