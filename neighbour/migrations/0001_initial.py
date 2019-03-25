# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20)),
                ('occupants', models.CharField(max_length=30)),
            ],
        ),
    ]
