# Generated by Django 4.2.10 on 2024-05-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_iron_player_alter_iron_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='iron',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-05-23T11:08:08.995279Z', verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iron',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]