# Generated by Django 3.1.1 on 2021-05-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210320_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
    ]
