# Generated by Django 3.1.1 on 2021-01-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0029_auto_20210128_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='made_in_africa',
        ),
        migrations.AddField(
            model_name='product',
            name='made_in_afrika',
            field=models.BooleanField(default=False, help_text='Is the product you adding produced and manufactured in Afrika? If so, check this box'),
        ),
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('P', 'Paypal'), ('M', 'M-Pesa'), ('S', 'Stripe'), ('D', 'Debit Card'), ('C', 'Cash On Delivery')], max_length=2),
        ),
        migrations.AlterField(
            model_name='brand',
            name='business_type',
            field=models.CharField(blank=True, choices=[('Co', 'Company'), ('Sol', 'Sole Proprietorship/Personal')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('U', 'Used'), ('N', 'New'), ('R', 'Refurbished'), ('C', 'Certified')], help_text='Choose the current condition for the product', max_length=2),
        ),
    ]
