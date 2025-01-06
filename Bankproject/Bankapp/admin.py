from django.contrib import admin
from . models import bankLoging,applogin,transaction_details

# Register your models here.
admin.site.register(applogin)
admin.site.register(bankLoging)
admin.site.register(transaction_details)