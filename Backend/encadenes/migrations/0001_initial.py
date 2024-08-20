# Generated by Django 4.2.14 on 2024-08-20 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Crag",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="State",
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
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="encadenes.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sector",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("total_routes", models.IntegerField(default=0)),
                (
                    "crag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="encadenes.crag"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Route",
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
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "rating",
                    models.DecimalField(decimal_places=2, default=0, max_digits=3),
                ),
                ("total_ascents", models.IntegerField(default=0)),
                ("recommended_by", models.IntegerField(default=0)),
                ("grado", models.CharField(default="000", max_length=10)),
                (
                    "sector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="encadenes.sector",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="crag",
            name="state",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="encadenes.state"
            ),
        ),
    ]
