from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('qr/', views.process_qr, name='process_qr'),    
    re_path(r'patron/(?P<nickname>[\s\w-]*)/?$', views.dashboard, name='dashboard'),
]
