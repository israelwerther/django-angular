# Generated by Django 4.2.10 on 2024-09-28 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_ironmine'),
    ]

    operations = [
        migrations.AddField(
            model_name='iron',
            name='mine',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.ironmine'),
        ),
    ]