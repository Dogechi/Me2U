# Generated by Django 3.1.1 on 2021-01-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0006_auto_20210122_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('M', 'M-Pesa'), ('D', 'Debit Card'), ('P', 'Paypal'), ('C', 'Cash On Delivery'), ('S', 'Stripe')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('N', 'New'), ('C', 'Certified'), ('U', 'Used'), ('R', 'Refurbished')], help_text='Choose the current condition for the product', max_length=2),
        ),
    ]
