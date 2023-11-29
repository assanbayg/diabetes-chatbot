# Generated by Django 4.2.7 on 2023-11-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BloodLevelEntry",
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
                ("level", models.FloatField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
