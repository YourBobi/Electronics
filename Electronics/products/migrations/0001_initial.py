# Generated by Django 4.2.6 on 2023-10-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("date", models.DateTimeField()),
                ("product_model", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "db_table": "Products",
            },
        ),
    ]