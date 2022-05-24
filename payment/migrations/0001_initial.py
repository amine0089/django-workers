# Generated by Django 2.0.4 on 2020-04-21 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('approved', 'approved'), ('not_approved', 'not approved')], max_length=255)),
                ('money_spend', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Money Spend ($)')),
                ('date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_transactions', to='base.Client')),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_investors', to='base.Investment')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payment.PaymentMethod')),
            ],
        ),
        migrations.CreateModel(
            name='UserPaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_payments_methods', to='base.Client')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.PaymentMethod')),
            ],
        ),
    ]
