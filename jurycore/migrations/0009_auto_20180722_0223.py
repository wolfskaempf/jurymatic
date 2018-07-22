# Generated by Django 2.0.7 on 2018-07-22 00:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('jurycore', '0008_auto_20180722_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('cf7bf30e-9314-4611-a82c-060bf60508ae'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('5f61e6aa-f943-44a6-831e-eb958ecc2b6b'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='delegation',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('418a3c9f-cd1c-4b8f-bb63-5e9209227d7e'), editable=False, unique=True),
        ),
    ]