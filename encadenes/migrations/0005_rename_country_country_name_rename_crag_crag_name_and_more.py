# Generated by Django 4.2.14 on 2024-08-06 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("encadenes", "0004_alter_route_sector"),
    ]

    operations = [
        migrations.RenameField(
            model_name="country",
            old_name="country",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="crag",
            old_name="crag",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="route",
            old_name="route",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="sector",
            old_name="sector",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="state",
            old_name="state",
            new_name="name",
        ),
    ]