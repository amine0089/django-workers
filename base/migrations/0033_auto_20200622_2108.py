# Generated by Django 2.0.4 on 2020-06-22 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_auto_20200622_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_investment',
            name='invest_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date of investment'),
        ),
    ]
