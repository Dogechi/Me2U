# Generated by Django 3.1.1 on 2021-01-22 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_sellerprofile'),
        ('me2ushop', '0003_auto_20210120_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.sellerprofile'),
        ),
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('S', 'Stripe'), ('P', 'Paypal'), ('D', 'Debit Card'), ('C', 'Cash On Delivery'), ('M', 'M-Pesa')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('R', 'Refurbished'), ('C', 'Certified'), ('N', 'New'), ('U', 'Used')], help_text='Choose the current condition for the product', max_length=2),
        ),
    ]
