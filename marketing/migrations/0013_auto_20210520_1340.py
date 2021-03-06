# Generated by Django 3.1.1 on 2021-05-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0012_auto_20210411_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
        migrations.AlterField(
            model_name='marketingemails',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
        migrations.AlterField(
            model_name='marketingmessage',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
        migrations.AlterField(
            model_name='trend',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
        migrations.AlterField(
            model_name='trendinfo',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
    ]
