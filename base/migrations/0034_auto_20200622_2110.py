# Generated by Django 2.0.4 on 2020-06-22 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_auto_20200622_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_investment',
            name='invest_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of investment'),
        ),
    ]
