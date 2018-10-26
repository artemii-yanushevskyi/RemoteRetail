from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from ...retail.models import Purchase, Good, Wallet

User = get_user_model()


class PurchaseSerializer(ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'


class GoodSerializer(ModelSerializer):

    class Meta:
        model = Good
        fields = '__all__'


class WalletSerializer(ModelSerializer):

    class Meta:
        model = Wallet
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
