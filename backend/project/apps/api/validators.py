from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

User = get_user_model()


class EmailExistenceValidator(object):

    def __call__(self, coveted_email):
        queryset = User.objects.all()
        email_q = queryset.filter(email=coveted_email)
        if not email_q.exists():
            raise serializers.ValidationError(
                _('User with such email does not exist.')
            )
