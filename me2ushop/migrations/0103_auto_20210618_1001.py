# Generated by Django 3.1.1 on 2021-06-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0102_auto_20210618_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('M', 'M-Pesa'), ('P', 'Paypal'), ('S', 'Stripe')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Please note that the default currency is USD. Converty your product price to US dollar before listing', max_digits=9),
        ),
    ]
