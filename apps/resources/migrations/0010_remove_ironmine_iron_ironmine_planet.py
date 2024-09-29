# Generated by Django 4.2.10 on 2024-09-29 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0004_remove_planet_iron'),
        ('resources', '0009_remove_iron_mine_ironmine_iron'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ironmine',
            name='iron',
        ),
        migrations.AddField(
            model_name='ironmine',
            name='planet',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mine', to='planets.planet'),
            preserve_default=False,
        ),
    ]
