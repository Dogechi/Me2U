# Generated by Django 3.0.7 on 2020-07-27 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='seller_profile',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
