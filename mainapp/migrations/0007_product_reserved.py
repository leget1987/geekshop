# Generated by Django 2.2.16 on 2020-11-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reserved',
            field=models.PositiveIntegerField(default=0, verbose_name='зарезервировано'),
        ),
    ]
