# Generated by Django 2.0.7 on 2018-07-23 19:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('jurycore', '0015_auto_20180722_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklet',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
