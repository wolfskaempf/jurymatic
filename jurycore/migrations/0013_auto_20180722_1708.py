# Generated by Django 2.0.7 on 2018-07-22 15:08

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jurycore', '0012_auto_20180722_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegation',
            name='colour',
            field=colorful.fields.RGBColorField(blank=True, default='#fff'),
        ),
    ]
