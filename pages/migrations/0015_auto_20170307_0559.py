# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-07 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20170303_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='keywords',
            new_name='meta_data',
        ),
        migrations.RemoveField(
            model_name='page',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='page',
            name='meta_title',
        ),
    ]
