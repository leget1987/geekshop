# Generated by Django 2.2.16 on 2020-11-28 13:37

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0011_auto_20201123_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 13, 37, 8, 531421, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]