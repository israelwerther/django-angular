# Generated by Django 4.2.10 on 2024-08-01 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='iron',
        ),
    ]
