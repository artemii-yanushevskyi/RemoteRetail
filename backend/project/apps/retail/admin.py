from django.contrib import admin

from .models import Good, Purchase, Wallet


admin.site.register(Good)
admin.site.register(Purchase)
admin.site.register(Wallet)
