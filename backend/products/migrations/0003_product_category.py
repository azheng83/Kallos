# Generated by Django 4.2.5 on 2023-11-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_heroimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(default="Uncategorized", max_length=200),
        ),
    ]
