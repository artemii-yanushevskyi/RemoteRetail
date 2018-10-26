"""
Django apps settings.
"""

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'raven.contrib.django.raven_compat',
    'debug_toolbar',
    'rest_framework',
    'rest_framework_swagger',
    'django_filters',
    # In case of building api
    'corsheaders',

    'apps.retail',
    'apps.core',
]

# Site framework
SITE_ID = 1

# CORS
CORS_ORIGIN_ALLOW_ALL = True
