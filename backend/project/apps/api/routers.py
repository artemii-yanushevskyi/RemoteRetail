"""
Api routers are defined here.
"""
from django.conf.urls import url, include

from rest_framework import routers

from .views import PurchasesViewSet, GoodViewSet, UserViewSet, WalletViewSet

router = routers.DefaultRouter()

# General
router.register(r'purchases', PurchasesViewSet, base_name='purchase')
router.register(r'goods', GoodViewSet, base_name='good')
router.register(r'users', UserViewSet, base_name='user')
router.register(r'wallets', WalletViewSet, base_name='wallet')

router_patterns = [
    url(r'^', include(router.urls)),
]
