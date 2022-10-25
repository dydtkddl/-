# Generated by Django 4.1.1 on 2022-10-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("email", models.CharField(max_length=50)),
                ("pwd", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=10)),
            ],
        ),
    ]
