# Generated by Django 3.2.6 on 2021-09-03 14:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20210831_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_bank', models.FloatField(default=500)),
                ('amount_spent', models.FloatField(default=0)),
                ('amount_made', models.FloatField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AlterField(
            model_name='reciperequirment',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ingredient'),
        ),
    ]
