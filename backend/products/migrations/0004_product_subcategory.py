# Generated by Django 4.2.5 on 2023-11-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="subcategory",
            field=models.CharField(default="Uncategorized", max_length=200),
        ),
    ]
