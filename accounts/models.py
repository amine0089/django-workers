from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

User = get_user_model()
ENTITY_TYPES = (
    ('Company', 'Company'),
    ('Trust', 'Trust'),
    ('Institutional account', 'Institutional account'),
    ('Other entity', 'Other entity')
)

ACCOUNT_TYPES = (
    ('Checking', 'Checking'),
    ('Saving', 'Saving'),
    ('Retirement', 'Retirement')
)
 

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    legal_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    zip = models.IntegerField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16 ,null=True, blank=True)
    bank_name = models.CharField(max_length=255)
    swift_code = models.CharField(max_length=255)
    ABA_number = models.IntegerField(default=0)  # Only when country is USA
    SSN = models.CharField(max_length=255)  # Only when country is USA
    notes = models.TextField(null=True)
    token = models.CharField(max_length=40)

    # investments, association table
    # payment_method, association table

    def __str__(self):
        return self.legal_name


class Private(Client):
    # Account, association table

    def __str__(self):
        return self.legal_name


class Entity(Client):
    type = models.CharField(max_length=255, choices=ENTITY_TYPES)

    def __str__(self):
        return self.legal_name
    
    class Meta:
        verbose_name='Entitie'


class Account(models.Model):
    type = models.CharField(max_length=255, choices=ACCOUNT_TYPES)
    account_number = models.IntegerField(unique=True)  # Tell if it has some validation for this field.
    funds = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Funds ($)', default=0)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='my_accounts')

    def __str__(self):
        return str(self.account_number)
