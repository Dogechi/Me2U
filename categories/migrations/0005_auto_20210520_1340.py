# Generated by Django 3.1.1 on 2021-05-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_remove_department_sub_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
    ]
