# Generated by Django 3.1.1 on 2021-01-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210129_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerprofile',
            name='phone',
            field=models.CharField(help_text='This number will be visible to buyers who would like to contact you for services. i.e +250785011413', max_length=20, unique=True),
        ),
    ]
