# Generated by Django 5.0.1 on 2024-01-03 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_info', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cats',
            new_name='Cat',
        ),
    ]
