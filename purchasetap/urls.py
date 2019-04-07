from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_seller, name='login'),
    path('logout', views.logout_view, name='logout'),
    re_path(r'^ajax/count/?$', views.count, name='count'),
]
