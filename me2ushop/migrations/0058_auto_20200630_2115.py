# Generated by Django 3.0.7 on 2020-06-30 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me2ushop', '0057_auto_20200630_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='cart_id',
        ),
        migrations.DeleteModel(
            name='CartID',
        ),
    ]
