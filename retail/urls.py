from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    re_path(r'(?P<nickname>[\s\w-]*)/?$', views.dashboard, name='dashboard'),
    
    path('qr/', views.process_qr, name='process_qr'),    
]
