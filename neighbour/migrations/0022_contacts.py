# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0021_auto_20190325_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=30)),
                ('police', models.CharField(max_length=30)),
            ],
        ),
    ]
