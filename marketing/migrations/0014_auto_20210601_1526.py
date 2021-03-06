# Generated by Django 3.1.1 on 2021-06-01 13:26

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0013_auto_20210520_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slider_type',
            field=models.CharField(blank=True, choices=[('La', 'Landing page'), ('Ho', 'Home page')], max_length=2, null=True),
        ),
        migrations.CreateModel(
            name='SliderImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True, verbose_name='creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='images/marketing/slider')),
                ('image_url', models.CharField(blank=True, max_length=250, null=True)),
                ('background_image_url', models.CharField(blank=True, max_length=250, null=True)),
                ('link_url', models.CharField(blank=True, max_length=250, null=True)),
                ('background_image', stdimage.models.StdImageField(blank=True, null=True, upload_to='images/marketing/banner')),
                ('in_display', models.BooleanField(default=True)),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.slider')),
            ],
            options={
                'ordering': ('-in_display',),
            },
        ),
    ]
