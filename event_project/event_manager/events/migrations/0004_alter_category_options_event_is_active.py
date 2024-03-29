# Generated by Django 4.2.9 on 2024-01-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategorie', 'verbose_name_plural': 'Kategorien'},
        ),
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
