# Generated by Django 4.0.5 on 2022-06-26 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_remove_measurement_id_sensor_chain_id_sensor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='image',
        ),
    ]
