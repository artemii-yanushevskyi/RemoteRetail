from django.contrib.auth import get_user_model

from rest_framework.viewsets import ReadOnlyModelViewSet

from ...retail.models import Purchase, Good, Wallet
from ..serializers import (
    PurchaseSerializer, GoodSerializer, WalletSerializer, UserSerializer
)

User = get_user_model()


class PurchasesViewSet(ReadOnlyModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class GoodViewSet(ReadOnlyModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class WalletViewSet(ReadOnlyModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
