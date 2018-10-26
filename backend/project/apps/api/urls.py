from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import UserDetails, EmailExistence, ResetPassword

from . import routers

from .routers import router_patterns



urlpatterns = [
    url(r'^auth/login', obtain_jwt_token, name='auth-token'),
    url(r'^auth/refresh-token', refresh_jwt_token, name='refresh-token'),
    url(r'^auth/verify-token', verify_jwt_token, name='verify-token'),
    url(r'^auth/user', UserDetails.as_view(), name='user-details'),
    url(r'^auth/reset-password', ResetPassword.as_view(),
        name='reset-password'),
    url(r'^utils/email-existence', EmailExistence.as_view(),
        name='email-existence'),


    url(r'^', include(routers.router.urls)),

    # url(r'^auth/forgot-password', forgot_password, name='forgot-password'),

    url(r'', include(router_patterns)),
]
