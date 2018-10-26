"""
Cache settings.
"""

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 5
CACHE_MIDDLEWARE_KEY_PREFIX = 'django'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'local_memory_cache',
        'TIMEOUT': CACHE_MIDDLEWARE_SECONDS,
        'OPTIONS': {
            'MAX_ENTRIES': 100000
        }
    }
}
