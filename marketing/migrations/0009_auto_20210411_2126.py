# Generated by Django 3.1.1 on 2021-04-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0008_auto_20210411_2112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['-modified']},
        ),
    ]
