# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0006_remove_rental_whoo'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='whoo',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]
