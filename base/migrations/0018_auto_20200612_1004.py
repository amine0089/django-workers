# Generated by Django 2.0.4 on 2020-06-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_investment_current_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='current_state',
            field=models.CharField(choices=[('In renovation', 'In renovation'), ('In construction', 'In construction'), ('Closing period', 'Closing period'), ('Performing asset', 'Performing asset')], max_length=255, null=True),
        ),
    ]
