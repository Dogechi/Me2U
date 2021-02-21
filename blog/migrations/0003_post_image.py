# Generated by Django 3.1.1 on 2021-02-18 19:59

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='images/products'),
        ),
    ]
