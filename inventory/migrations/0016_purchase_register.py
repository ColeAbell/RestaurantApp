# Generated by Django 3.2.6 on 2021-09-06 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_remove_purchase_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='register',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.register'),
            preserve_default=False,
        ),
    ]