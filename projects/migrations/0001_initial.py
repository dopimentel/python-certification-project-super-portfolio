# Generated by Django 4.2.3 on 2024-05-04 02:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=100)),
                ("github", models.URLField()),
                ("linkedin", models.URLField()),
                ("bio", models.TextField()),
            ],
        ),
    ]
