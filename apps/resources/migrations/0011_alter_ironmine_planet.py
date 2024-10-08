# Generated by Django 4.2.10 on 2024-09-29 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0004_remove_planet_iron'),
        ('resources', '0010_remove_ironmine_iron_ironmine_planet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ironmine',
            name='planet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='iron_mine', to='planets.planet'),
        ),
    ]
