# Generated by Django 3.2.6 on 2021-08-22 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210822_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='description',
            new_name='unit_size',
        ),
    ]