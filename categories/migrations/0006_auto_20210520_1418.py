# Generated by Django 3.1.1 on 2021-05-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_auto_20210520_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='is_active',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
