# Generated by Django 3.1.1 on 2020-10-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0014_auto_20201008_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('M', 'M-Pesa'), ('C', 'Cash On Delivery'), ('S', 'Stripe'), ('D', 'Debit Card'), ('P', 'Paypal')], max_length=2),
        ),
    ]