"""
Root urls.
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render
from django.views.static import serve

from rest_framework_swagger.views import get_swagger_view

admin.site.site_header = 'Application Administration'
admin.site.site_title = 'Application Administration'

SCHEMA_VIEW = get_swagger_view(
    title='Application API',
)


def home(request):
    """Home view."""
    return render(request, 'home.html')

urlpatterns = [
    url(r'^$', home),
    url(r'^api/', include(('apps.api.urls', 'apps.api'), namespace='api')),
]

if settings.ADMIN_PANEL_AVAILABLE:
    urlpatterns += [
        url(r'^admin/', admin.site.urls)
    ]

if settings.SHOW_API_DOCS:
    urlpatterns += [
        url(r'^swagger/$', SCHEMA_VIEW),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]

if settings.SERVE_STATIC_IN_APP:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        })
    ]
