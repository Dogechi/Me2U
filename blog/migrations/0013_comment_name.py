# Generated by Django 3.1.1 on 2021-03-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210319_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='daniel Ogechi', max_length=55),
            preserve_default=False,
        ),
    ]
