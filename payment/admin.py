from django.contrib import admin
from payment.models import *

# Register your models here.
admin.site.register(PaymentMethod)
admin.site.register(UserPaymentMethod)
admin.site.register(Transation)