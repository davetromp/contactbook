# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_index=True, max_length=255)),
                ('lastname', models.CharField(db_index=True, max_length=255)),
                ('street', models.CharField(db_index=True, max_length=255)),
                ('zipcode', models.CharField(db_index=True, max_length=255)),
                ('city', models.CharField(db_index=True, max_length=255)),
                ('image_url', models.CharField(db_index=True, max_length=255)),
            ],
        ),
    ]
