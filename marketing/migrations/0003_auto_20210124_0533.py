# Generated by Django 3.1.1 on 2021-01-24 03:33

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20201215_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='banner_background',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='banner_background',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='banner_image',
        ),
        migrations.AddField(
            model_name='banner',
            name='background_image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='images/marketing/banner'),
        ),
        migrations.AddField(
            model_name='banner',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='images/marketing/banner'),
        ),
        migrations.AddField(
            model_name='slider',
            name='background_image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='images/marketing/banner'),
        ),
    ]