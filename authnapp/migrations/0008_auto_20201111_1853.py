# Generated by Django 2.2.16 on 2020-11-11 18:53

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0007_auto_20201111_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 18, 53, 58, 800268, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
