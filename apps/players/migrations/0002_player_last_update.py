# Generated by Django 4.2.10 on 2024-05-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
