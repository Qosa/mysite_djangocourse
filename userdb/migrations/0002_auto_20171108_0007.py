# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='surname',
        ),
    ]
