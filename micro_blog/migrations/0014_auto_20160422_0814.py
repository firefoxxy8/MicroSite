# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_blog', '0013_auto_20160303_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_file',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='static/uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='image_file',
            name='upload',
            field=models.FileField(upload_to='static/uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta_description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('D', 'Draft'), ('P', 'Published'), ('T', 'Rejected'), ('R', 'Review')], max_length=2),
        ),
    ]
