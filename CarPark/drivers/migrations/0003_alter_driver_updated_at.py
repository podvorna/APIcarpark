# Generated by Django 4.0 on 2021-12-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_driver_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
