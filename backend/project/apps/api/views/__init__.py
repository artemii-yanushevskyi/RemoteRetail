from django.contrib.auth import get_user_model

from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from ...retail.models import Purchase, Good, Wallet
from ..serializers import (
    PurchaseSerializer, GoodSerializer, WalletSerializer, UserSerializer
)

User = get_user_model()


class UserDetails(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        data = UserSerializer(request.user).data
        return Response(data={'status': 'success', 'data': data})


class ResetPassword(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request: Request):
        user = request.user
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not user.check_password(serializer.data['old_password']):
            raise ValidationError(_('Wrong current password entered.'))
        request.user.set_password(serializer.data['new_password'])
        request.user.save()
        return Response(data={
            'message': _('Password was changed successfully.')
        })


class EmailExistence(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = EmailExistenceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response()


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
