# Generated by Django 4.2.2 on 2023-06-29 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0010_rename_emplois_du_temps1_emplois_du_temps_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Emplois_du_temps2',
        ),
        migrations.DeleteModel(
            name='Emplois_du_temps3',
        ),
    ]
