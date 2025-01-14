# Generated by Django 5.1.1 on 2024-09-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WeatherData",
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
                ("city", models.CharField(max_length=100)),
                ("temperature", models.FloatField()),
                ("humidity", models.IntegerField()),
                ("condition", models.CharField(max_length=100)),
                ("wind_speed", models.FloatField()),
                ("last_updated", models.DateTimeField()),
            ],
        ),
    ]
