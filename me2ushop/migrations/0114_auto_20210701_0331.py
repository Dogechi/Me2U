# Generated by Django 3.1.1 on 2021-07-01 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangorave', '0001_initial'),
        ('me2ushop', '0113_auto_20210630_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='active',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('S', 'Stripe'), ('M', 'M-Pesa'), ('P', 'Paypal')], max_length=2),
        ),
        migrations.AlterField(
            model_name='brand',
            name='subscription_plan',
            field=models.ForeignKey(blank=True, help_text='Select a monthly recurring subscription fees', null=True, on_delete=django.db.models.deletion.SET_NULL, to='djangorave.drpaymenttypemodel'),
        ),
    ]
