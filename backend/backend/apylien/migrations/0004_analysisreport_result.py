# Generated by Django 3.0.1 on 2020-01-03 01:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apylien', '0003_auto_20200102_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisreport',
            name='result',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
