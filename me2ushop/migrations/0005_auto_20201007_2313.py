# Generated by Django 3.1.1 on 2020-10-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0004_auto_20201007_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('P', 'Paypal'), ('D', 'Debit Card'), ('S', 'Stripe'), ('M', 'M-Pesa'), ('C', 'Cash On Delivery')], max_length=2),
        ),
    ]