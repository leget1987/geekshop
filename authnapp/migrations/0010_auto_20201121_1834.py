# Generated by Django 2.2.16 on 2020-11-21 18:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0009_auto_20201121_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 18, 34, 19, 951719, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]