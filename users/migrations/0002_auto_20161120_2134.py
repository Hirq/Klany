# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bibliouser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='bibliouser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='BiblioUser',
        ),
    ]
