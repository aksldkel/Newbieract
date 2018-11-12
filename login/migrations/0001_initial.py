# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-07 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('member_name', models.CharField(blank=True, max_length=15, null=True)),
                ('pwd', models.CharField(blank=True, max_length=32, null=True)),
                ('meta_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Member',
            },
        ),
    ]
