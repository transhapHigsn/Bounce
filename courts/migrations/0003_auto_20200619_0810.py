# Generated by Django 3.0.7 on 2020-06-19 13:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_auto_20200619_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='id',
            field=models.CharField(default=uuid.UUID('9ab9564b-c508-4ff1-96eb-1002dec7421b'), max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='court',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=None, srid=4326),
        ),
    ]