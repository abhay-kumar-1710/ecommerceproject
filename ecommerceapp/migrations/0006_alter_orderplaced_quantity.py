# Generated by Django 5.0.6 on 2024-09-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0005_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
