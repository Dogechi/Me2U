# Generated by Django 3.1.1 on 2021-01-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210123_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerprofile',
            name='business_description',
            field=models.TextField(default='me2uafrika'),
            preserve_default=False,
        ),
    ]
