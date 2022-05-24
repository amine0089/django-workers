# Generated by Django 2.0.4 on 2020-06-22 23:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_investment_swift_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distribution_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Distribution date')),
                ('distributed_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Distributed amount')),
                ('roi', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Return On Investment (%)')),
                ('investment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Investment')),
            ],
        ),
    ]
