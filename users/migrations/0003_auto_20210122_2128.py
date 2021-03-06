# Generated by Django 3.1.1 on 2021-01-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_sellerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerprofile',
            name='email',
            field=models.EmailField(blank=True, help_text='Provide Business email where customers can send inquries', max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='facebook_page',
            field=models.CharField(blank=True, help_text='Do you have a facebook page. Copy paste your page link here e.g.. https://www.facebook.com/Me2UAfrika', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='instagram',
            field=models.CharField(blank=True, help_text='Do you have a instagram page. Copy paste your page link here eg. https://www.instagram.com/me2u_afrika/', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='phone',
            field=models.CharField(blank=True, help_text='This number will be visible to buyers who would like to contact you for services. i.e +250785011413', max_length=20, null=True),
        ),
    ]
