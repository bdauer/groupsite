# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupsite', '0003_auto_20170312_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='facebook_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='google_id',
        ),
    ]