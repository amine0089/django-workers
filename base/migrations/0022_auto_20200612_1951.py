# Generated by Django 2.0.4 on 2020-06-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20200612_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_investment',
            name='payment_token',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
