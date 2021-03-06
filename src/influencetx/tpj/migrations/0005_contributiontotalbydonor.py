# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-28 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tpj', '0004_contributionsummary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributiontotalbydonor',
            fields=[
                ('donor', models.OneToOneField(db_column='ctrib_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tpj.Donor')),
                ('election_year', models.IntegerField(blank=True, db_column='eYear', null=True)),
                ('cycle_total', models.DecimalField(blank=True, db_column='cycle_total', decimal_places=2, max_digits=19, null=True)),
            ],
            options={
                'db_table': 'total_donor',
                'managed': False,
            },
        ),
    ]
