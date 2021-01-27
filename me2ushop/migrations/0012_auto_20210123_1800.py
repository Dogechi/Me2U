# Generated by Django 3.1.1 on 2021-01-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0011_auto_20210123_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('D', 'Debit Card'), ('S', 'Stripe'), ('M', 'M-Pesa'), ('P', 'Paypal'), ('C', 'Cash On Delivery')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('U', 'Used'), ('C', 'Certified'), ('R', 'Refurbished'), ('N', 'New')], help_text='Choose the current condition for the product', max_length=2),
        ),
    ]