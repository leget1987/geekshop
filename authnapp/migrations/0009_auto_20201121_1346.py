# Generated by Django 2.2.16 on 2020-11-21 13:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0008_auto_20201111_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 13, 46, 55, 884237, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]