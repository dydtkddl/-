# Generated by Django 4.1 on 2022-10-26 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0004_article"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileAttach",
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
                ("o_filename", models.CharField(max_length=1000)),
                ("save_filename", models.CharField(max_length=1000)),
                ("filesize", models.IntegerField(default=0)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="article.article",
                    ),
                ),
            ],
        ),
    ]
