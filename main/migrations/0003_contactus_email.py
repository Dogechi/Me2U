# Generated by Django 3.1.1 on 2021-03-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_madere_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default='danielmakori0@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]