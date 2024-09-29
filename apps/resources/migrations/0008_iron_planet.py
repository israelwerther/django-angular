# Generated by Django 4.2.10 on 2024-09-28 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0004_remove_planet_iron'),
        ('resources', '0007_alter_ironmine_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='iron',
            name='planet',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='iron', to='planets.planet'),
            preserve_default=False,
        ),
    ]
