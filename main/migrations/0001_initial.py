# Generated by Django 3.0.7 on 2020-08-14 05:26

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(10, 'Open'), (20, 'Submitted')], default=10)),
            ],
        ),
        migrations.CreateModel(
            name='BasketLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='MaDere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Namba', models.CharField(max_length=13)),
                ('price_per_km', models.FloatField()),
                ('location', models.CharField(max_length=255)),
                ('availability', models.BooleanField()),
                ('image_url', models.CharField(blank=True, max_length=2083, null=True)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image_Ndai', models.ImageField(blank=True, null=True, upload_to='Ma_Ndai')),
                ('license_verified', models.BooleanField(default=False)),
                ('type_of_automobile', models.CharField(choices=[('BI', 'Baiskeli'), ('MK', 'MotorBike'), ('CR', 'Car'), ('LO', 'Lorry')], max_length=2)),
                ('customers', models.CharField(choices=[('A', 'Passengers'), ('M', 'Mizigo')], max_length=1)),
            ],
        ),
    ]
