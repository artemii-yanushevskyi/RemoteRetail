"""
Development environment settings.
"""
import datetime

ENVIRONMENT_NAME = 'Development'
ENVIRONMENT_COLOR = 'green'

DEBUG = True

SHOW_API_DOCS = True

ADMIN_PANEL_AVAILABLE = True

SERVE_STATIC_IN_APP = True

INSTALLED_APPS += [
    'django.contrib.admin',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

JWT_AUTH['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=28)
