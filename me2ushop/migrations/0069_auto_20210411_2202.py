# Generated by Django 3.1.1 on 2021-04-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0068_auto_20210411_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('C', 'Cash On Delivery'), ('S', 'Stripe'), ('M', 'M-Pesa'), ('D', 'Debit Card'), ('P', 'Paypal')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('U', 'Used'), ('N', 'New'), ('R', 'Refurbished')], help_text='Choose the current condition for the product', max_length=2),
        ),
    ]