# Generated by Django 3.1.1 on 2021-01-25 04:00

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_auto_20210124_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendinfo',
            name='trend_background',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='images/marketing/banner'),
        ),
    ]
