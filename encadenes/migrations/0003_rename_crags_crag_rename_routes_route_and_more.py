# Generated by Django 4.2.14 on 2024-08-06 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("encadenes", "0002_alter_sectors_total_routes"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Crags",
            new_name="Crag",
        ),
        migrations.RenameModel(
            old_name="Routes",
            new_name="Route",
        ),
        migrations.RenameModel(
            old_name="Sectors",
            new_name="Sector",
        ),
        migrations.RenameModel(
            old_name="States",
            new_name="State",
        ),
    ]