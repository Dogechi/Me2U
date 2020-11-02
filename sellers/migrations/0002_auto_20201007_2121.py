# Generated by Django 3.1.1 on 2020-10-07 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellers',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='businessinformation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.sellers'),
        ),
    ]