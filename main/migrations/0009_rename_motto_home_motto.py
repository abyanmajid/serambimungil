# Generated by Django 4.1.3 on 2023-02-01 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_home'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='Motto',
            new_name='motto',
        ),
    ]
