# Generated by Django 2.0.4 on 2020-06-22 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_distribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='investment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='my_distributions', to='base.Investment'),
        ),
    ]