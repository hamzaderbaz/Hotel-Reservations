# Generated by Django 4.2.7 on 2023-12-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_rename_title_property_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]