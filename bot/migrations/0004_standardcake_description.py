# Generated by Django 5.1.4 on 2025-03-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_standardcake_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardcake',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание торта'),
        ),
    ]
