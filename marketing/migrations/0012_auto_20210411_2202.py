# Generated by Django 3.1.1 on 2021-04-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0011_auto_20210411_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trend',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
