# Generated by Django 3.1.1 on 2021-01-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('me2ushop', '0024_auto_20210128_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='main_category',
            new_name='category_choice',
        ),
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('C', 'Cash On Delivery'), ('M', 'M-Pesa'), ('S', 'Stripe'), ('P', 'Paypal'), ('D', 'Debit Card')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('U', 'Used'), ('C', 'Certified'), ('N', 'New'), ('R', 'Refurbished')], help_text='Choose the current condition for the product', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_categories',
            field=models.ManyToManyField(blank=True, help_text='Check the box of the category where your product belongs. Please note that different categories attract different Ad charges. Be specific to one or two categories where your product belongs on the provided tree. Contact us for help', to='categories.Department'),
        ),
    ]