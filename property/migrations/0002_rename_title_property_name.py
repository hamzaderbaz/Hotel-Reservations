# Generated by Django 4.2.7 on 2023-12-12 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='title',
            new_name='name',
        ),
    ]
