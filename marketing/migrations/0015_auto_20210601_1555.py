# Generated by Django 3.1.1 on 2021-06-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0014_auto_20210601_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='slider_type',
            field=models.CharField(blank=True, choices=[('La', 'Landing page'), ('Ho', 'Home page')], default='La', max_length=2, null=True, unique=True),
        ),
    ]
