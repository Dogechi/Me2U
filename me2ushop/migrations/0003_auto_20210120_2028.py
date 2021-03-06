# Generated by Django 3.1.1 on 2021-01-20 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0002_auto_20201215_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('R', 'Refurbished'), ('C', 'Certified'), ('U', 'Used'), ('N', 'New')], default='N', help_text='Choose the current condition for the product', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('C', 'Cash On Delivery'), ('D', 'Debit Card'), ('S', 'Stripe'), ('M', 'M-Pesa'), ('P', 'Paypal')], max_length=2),
        ),
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, verbose_name='creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('book_start', models.DateTimeField(auto_now_add=True, null=True)),
                ('book_end', models.DateTimeField(auto_now_add=True, null=True)),
                ('rental_price_day', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount_per_week', models.IntegerField(blank=True, null=True)),
                ('discount_per_month', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='me2ushop.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
