# Generated by Django 3.1.1 on 2020-11-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0020_remove_trend_trend_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='trend',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]