# Generated by Django 3.1.1 on 2020-11-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0061_auto_20201116_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('C', 'Cash On Delivery'), ('S', 'Stripe'), ('M', 'M-Pesa'), ('D', 'Debit Card'), ('P', 'Paypal')], max_length=2),
        ),
    ]