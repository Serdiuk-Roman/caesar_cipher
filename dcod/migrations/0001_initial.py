# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-08 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=4)),
                ('text', models.TextField()),
            ],
        ),
    ]
