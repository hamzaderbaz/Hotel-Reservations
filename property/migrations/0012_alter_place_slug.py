# Generated by Django 4.2.7 on 2024-01-20 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_place_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(),
        ),
    ]