# Generated by Django 4.1 on 2023-02-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart_shop", "0003_alter_product_discount_alter_product_price_after"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="discount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price_after",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
