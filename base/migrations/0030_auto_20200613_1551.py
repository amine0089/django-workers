# Generated by Django 2.0.4 on 2020-06-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_remove_client_investment_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='bank_address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investment',
            name='beneficiary_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
