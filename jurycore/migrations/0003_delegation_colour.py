# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-18 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurycore', '0002_delegate_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegation',
            name='colour',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
