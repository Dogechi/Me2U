# Generated by Django 3.0.7 on 2020-07-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200719_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
