# Generated by Django 4.2.10 on 2024-05-25 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
        ('players', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='iron',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='player_iron', to='resources.iron'),
            preserve_default=False,
        ),
    ]
