# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 17:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Rental', '0007_rental_whoo'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='who',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
