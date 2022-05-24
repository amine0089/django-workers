from django.db import models
from base.models import Client, Investment

# Create your models here.


STATUS = (
    ('approved', 'approved'),
    ('not_approved', 'not approved')
)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UserPaymentMethod(models.Model):  # Association table (Have) between Client and PaymentMethod
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='my_payments_methods')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return f'Client {self.client.legal_name} can pay with {self.payment_method.name}'


class Transation(models.Model):  # Association table between Client and Investment
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='my_transactions')
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='my_investors')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255, choices=STATUS)
    money_spend = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Money Spend ($)')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client.legal_name}  invest on  {self.investment.name}'
