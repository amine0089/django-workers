# Generated by Django 2.0.4 on 2020-06-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20200612_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_investment',
            name='status',
            field=models.CharField(choices=[('Not achieved', 'Not achieved'), ('Pending', 'Pending'), ('Complete', 'Complete')], default='Not achieved', max_length=12),
        ),
    ]