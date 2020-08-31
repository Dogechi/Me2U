# Generated by Django 3.0.7 on 2020-08-30 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0003_auto_20200829_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('M', 'M-Pesa'), ('S', 'Stripe'), ('P', 'Paypal'), ('C', 'Cash On Delivery'), ('D', 'Debit Card')], max_length=2),
        ),
    ]
