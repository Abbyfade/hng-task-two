# Generated by Django 4.1.2 on 2022-11-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Operation",
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
                ("operation_type", models.CharField(default="addition", max_length=15)),
                ("x", models.IntegerField()),
                ("y", models.IntegerField()),
            ],
        ),
    ]
