# Generated by Django 4.2.2 on 2023-06-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emplois_du_temps',
            name='Num_groupe',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emplois_du_temps',
            name='Salle',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
