# Generated by Django 2.2.8 on 2019-12-19 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_operacion_vol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operacion_vol',
            old_name='volumen',
            new_name='comando',
        ),
    ]
