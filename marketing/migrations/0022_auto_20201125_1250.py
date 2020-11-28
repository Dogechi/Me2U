# Generated by Django 3.1.1 on 2020-11-25 10:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0021_trend_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_discount_price',
            field=models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
    ]