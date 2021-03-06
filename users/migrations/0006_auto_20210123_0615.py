# Generated by Django 3.1.1 on 2021-01-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210122_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerprofile',
            name='telegram',
            field=models.CharField(blank=True, help_text='Do you have a Telegram Channel. Copy paste your page link here. e.g.. https://t.me/me2uafrika', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='website_link',
            field=models.CharField(blank=True, help_text='If you have a website by which buyers can find out more about your services.e.g. https://www.facebook.com', max_length=30, null=True),
        ),
    ]
