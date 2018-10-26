"""
Directories & files & paths settings.
"""
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_SERVER_PATH = os.environ.get('APP_DIR', BASE_DIR)

REPO_DIR = os.path.dirname(BASE_DIR)

ROOT_URLCONF = 'urls.urls'

WSGI_APPLICATION = 'wsgi.wsgi.application'

STATIC_URL = '/s/'

MEDIA_URL = '/media/'

if APP_SERVER_PATH == BASE_DIR:
    STATIC_ROOT = os.path.join(APP_SERVER_PATH, 'static-root')
    LOG_FILE = os.path.join(APP_SERVER_PATH, 'django-app.log')
else:
    STATIC_ROOT = os.path.join(APP_SERVER_PATH, 'static')
    LOG_FILE = os.path.join(APP_SERVER_PATH, 'logs', 'django-app.log')

MEDIA_ROOT = os.path.join(APP_SERVER_PATH, 'media')

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

UPLOAD_FOLDER = 'uploads/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
