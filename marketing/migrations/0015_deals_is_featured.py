# Generated by Django 3.1.1 on 2020-11-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0014_banner_top_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
