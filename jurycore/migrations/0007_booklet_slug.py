# Generated by Django 2.0.7 on 2018-07-21 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurycore', '0006_auto_20180721_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]