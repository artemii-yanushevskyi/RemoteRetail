from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from ..validators import EmailExistenceValidator
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
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'is_superuser', 'last_login', 'date_joined')
        read_only_fields = ('last_login', 'date_joined')


class EmailExistenceSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[EmailExistenceValidator(), ],
        write_only=True
    )


class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=1000)
    new_password = serializers.CharField(max_length=1000)
