# Generated by Django 3.1.5 on 2021-01-13 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confcheck', '0002_auto_20210113_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='IsDelete',
            new_name='IsDeleted',
        ),
    ]
