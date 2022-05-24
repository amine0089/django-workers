from django.contrib import admin
from base.models import *



# Register your models here.

class Client_InvestmentAdmin(admin.ModelAdmin):
    model = Client_Investment
    list_filter = ('investment__name', 'promocode', 'approved')
    list_display = ['investment', 'client', 'invest_date','status', 'approved', 'done', 'invested_amount', 'promocode']
 
class Client_InvestmentInline(admin.TabularInline):
    model = Client_Investment
    list_filter = ('investment__name',)


class PromoCodeAdmin(admin.ModelAdmin):
    inlines = [
        Client_InvestmentInline
    ]


class PropertyPictureInline(admin.TabularInline):
    model = PropertyPicture


class PromotionalDocumentInline(admin.TabularInline):
    model = PromotionalDocument

class DistributionInline(admin.TabularInline):
    model = Distribution


class InvestmentAdmin(admin.ModelAdmin):
    inlines = [
        PropertyPictureInline,
        PromotionalDocumentInline,
        DistributionInline
    ]
class PastprojectpictureInline(admin.TabularInline):
    model = Pastprojectpicture
class PastprojectPromotionalDocumentInline(admin.TabularInline):
    model = PastprojectPromotionalDocument

class PastprojectAdmin(admin.ModelAdmin):

    inlines = [
        PastprojectpictureInline,
        PastprojectPromotionalDocumentInline
    ]


admin.site.register(Client)
admin.site.register(Private)
admin.site.register(Entity)
admin.site.register(Account)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(Client_Investment, Client_InvestmentAdmin)
admin.site.register(Remark)
admin.site.register(PropertyPicture)
admin.site.register(PromotionalDocument)
admin.site.register(Testimonial)
admin.site.register(PromoCode, PromoCodeAdmin)
admin.site.register(Distribution)
admin.site.register(Pastproject, PastprojectAdmin)
