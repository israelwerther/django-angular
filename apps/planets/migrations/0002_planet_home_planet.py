# Generated by Django 4.2.10 on 2024-07-31 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='home_planet',
            field=models.BooleanField(default=False),
        ),
    ]
