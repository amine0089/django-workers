from django.db import models
from accounts.models import Client, Private, Entity, Account
from django.utils import timezone

# Create your models here.
STATUS = (
    ('Not achieved', 'Not achieved'),
    ('Pending', 'Pending'),
    ('Complete', 'Complete'),
)

STATES = (
    ('In renovation', 'In renovation'),
    ('In construction', 'In construction'),
    ('Closing period', 'Closing period'),
    ('Performing asset', 'Performing asset')
)


class Investment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    minimum_investment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Minimum investment ($)',
                                             default=0)
    gross_returns = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Gross returns (%)', default=0)
    net_returns = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Net returns (%)', default=0)
    description = models.TextField()
    invested_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Invested amount ($)',
                                          default=0)
    amount_needed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount needs in this fund',
                                        default=0)
    market_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Market value ($)', default=0)
    closed = models.BooleanField(default=False )
    SoloMartel_ownership = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='SoloMartel Ownership(%)', default=0)
    # ---------- Bank information -----------
    bank_name = models.CharField(max_length=255)
    bank_address = models.CharField(max_length=255)
    subsidiary_name = models.CharField(max_length=255)
    beneficiary_name = models.CharField(max_length=255)
    ABA_number = models.CharField(max_length=255)
    swift_code = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    account_number = models.IntegerField()  # Tell if it has some validation for this field.
    current_state = models.CharField(max_length=255, choices=STATES, null=True, blank=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.name


class Distribution(models.Model):
    distribution_date = models.DateTimeField(default=timezone.now, blank=True, verbose_name='Distribution date')
    distributed_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Distributed amount',
                                             default=0)
    roi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Return On Investment (%)', default=0)
    investment = models.ForeignKey(Investment, on_delete=models.DO_NOTHING, related_name='my_distributions')

    def __str__(self):
        return f'Distribution of: {self.distribution_date}'


class PromoCode(models.Model):
    code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    influencer_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.code


class Client_Investment(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='clients')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='investments')
    invest_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of investment')
    status = models.CharField(max_length=12, choices=STATUS, default='Not achieved')
    approved = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    invested_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Invested amount($)')
    payment_token = models.CharField(max_length=128, null=True, blank=True)
    promocode = models.ForeignKey(PromoCode, on_delete=models.DO_NOTHING, null=True, blank=True,
                                  related_name='clients_bring')

    class Meta:
        verbose_name = 'Transaction'

    def __str__(self):
        return f'{self.client.legal_name} invest in {self.investment.name}'


class Remark(models.Model):
    sender_email = models.EmailField()
    title = models.CharField(max_length=255)
    content = models.FileField(upload_to='remarks_files')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='my_remarks')

    def __str__(self):
        return self.title


class PropertyPicture(models.Model):
    name = models.CharField(max_length=255)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='my_images')
    image = models.ImageField(upload_to=f'investments/{investment.name}')

    def __str__(self):
        return f'{self.investment.name}[Image] - {self.name}'


class PromotionalDocument(models.Model):
    name = models.CharField(max_length=255)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='my_documents')
    file = models.FileField(upload_to=f'documents/{investment.name}')

    def __str__(self):
        return f'{self.investment.name}[Document] - {self.name}'


class Testimonial(models.Model):
    client_name = models.CharField(max_length=255, default='Satisfied client')
    client_photo = models.ImageField(upload_to='client_profile', null=True, blank=True)
    testimonial = models.TextField(blank=True)
    url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Testimonial {self.client_name}' if self.client_name else f'Testimonial {self.url}'

#Past Project Section

class Pastproject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    minimum_investment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Minimum investment ($)',
                                             default=0)
    gross_returns = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Gross returns (%)', default=0)
    net_returns = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Net returns (%)', default=0)
    description = models.TextField()
    invested_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Invested amount ($)',
                                          default=0)
    amount_needed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount needs in this fund',
                                        default=0)
    market_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Market value ($)', default=0)
    closed = models.BooleanField(default=False )
    SoloMartel_ownership = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='SoloMartel Ownership(%)', default=0)


    def __str__(self):
        return self.name


class Pastprojectpicture(models.Model):
    name = models.CharField(max_length=255)
    Pastproject = models.ForeignKey(Pastproject, on_delete=models.CASCADE, related_name='my_images')
    image = models.ImageField(upload_to=f'investments/{Pastproject.name}')

    def __str__(self):
        return f'{self.Pastproject.name} [Image] - {self.name}'

class PastprojectPromotionalDocument(models.Model):
    name = models.CharField(max_length=255)
    Pastproject = models.ForeignKey(Pastproject, on_delete=models.CASCADE, related_name='my_documents')
    file = models.FileField(upload_to=f'documents/{Pastproject.name}')

    def __str__(self):
        return f'{self.Pastproject.name} [Document] - {self.name}'