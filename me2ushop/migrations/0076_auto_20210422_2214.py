# Generated by Django 3.1.1 on 2021-04-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0075_auto_20210412_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('M', 'M-Pesa'), ('C', 'Cash On Delivery'), ('S', 'Stripe'), ('P', 'Paypal'), ('D', 'Debit Card')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('R', 'Refurbished'), ('U', 'Used'), ('N', 'New')], help_text='Choose the current condition for the product', max_length=2),
        ),
    ]