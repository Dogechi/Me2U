# Generated by Django 3.1.1 on 2021-02-03 14:15

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='icon_image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='images/category/icons'),
        ),
    ]