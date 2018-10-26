from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


from . import routers

from .routers import router_patterns



urlpatterns = [
    url(r'^auth/login', obtain_jwt_token, name='auth-token'),
    url(r'^auth/refresh-token', refresh_jwt_token, name='refresh-token'),
    url(r'^auth/verify-token', verify_jwt_token, name='verify-token'),


    url(r'^', include(routers.router.urls)),

    # url(r'^auth/forgot-password', forgot_password, name='forgot-password'),

    url(r'', include(router_patterns)),
]
