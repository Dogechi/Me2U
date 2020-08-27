# Generated by Django 3.0.7 on 2020-08-16 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0003_auto_20200814_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('C', 'Cash On Delivery'), ('M', 'M-Pesa'), ('P', 'Paypal'), ('D', 'Debit Card'), ('S', 'Stripe')], max_length=2),
        ),
    ]
