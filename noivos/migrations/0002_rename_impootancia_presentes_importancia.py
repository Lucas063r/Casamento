# Generated by Django 5.1.2 on 2024-11-05 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noivos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presentes',
            old_name='impootancia',
            new_name='importancia',
        ),
    ]
