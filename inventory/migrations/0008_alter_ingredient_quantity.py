# Generated by Django 3.2.6 on 2021-08-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_reciperequirment_menu_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.FloatField(default=20),
        ),
    ]
