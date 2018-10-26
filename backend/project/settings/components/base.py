"""
Base variables.
"""
import os

from django.utils.translation import ugettext_lazy as _

# ==============================================================================
# Base variables
# ==============================================================================

SECRET_KEY = 'SOME_VERY_SECRET_KEY'

DEBUG = str2bool(os.environ.get('DJANGO_DEBUG', 'False'))

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')

SHOW_API_DOCS = str2bool(os.environ.get('DJANGO_SHOW_API_DOCS', 'False'))

ADMIN_PANEL_AVAILABLE = str2bool(os.environ.get('DJANGO_ADMIN_PANEL_AVAILABLE', 'False'))

SERVE_STATIC_IN_APP = str2bool(os.environ.get('DJANGO_SERVE_STATIC_IN_APP', 'False'))

INTERNAL_IPS = [
    '127.0.0.1',
]

ALLOWED_HOSTS = []

ADMINS = [
    ('admin', 'admin@example.com'),
]

PREPEND_WWW = False

USE_ETAGS = True

ENVIRONMENT_NAME = 'Unknown, environment was not set'
ENVIRONMENT_COLOR = 'black'

# ==============================================================================
# Internationalization & Timezone
# ==============================================================================

LANGUAGE_CODE = 'en'

LANGUAGE_COOKIE_NAME = 'django-language'

LANGUAGES = [
    ('en', _('English')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ==============================================================================
# Authentication & Sessions
# ==============================================================================

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "default"
