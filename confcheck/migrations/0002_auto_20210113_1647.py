# Generated by Django 3.1.5 on 2021-01-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confcheck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='DataChange_CreateTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='DataChange_LastTime',
            field=models.DateTimeField(),
        ),
    ]