# Generated by Django 2.2.16 on 2020-11-04 14:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0003_default_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 14, 59, 6, 200359, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]