# Generated by Django 3.1.1 on 2021-05-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0081_auto_20210520_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('S', 'Stripe'), ('P', 'Paypal'), ('M', 'M-Pesa')], max_length=2),
        ),
    ]
