"""
Logging settings.
"""
import datetime

import raven

try:
    release = raven.fetch_git_sha(REPO_DIR)
except Exception:
    release = str(datetime.datetime.now())

RAVEN_DSN_URL = 'https://code1:code2@example.com/123456'
RAVEN_CONFIG = {
    'dsn': RAVEN_DSN_URL,
    'release': release,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOG_FILE,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 365,
            'utc': True,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['log_file', ],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['log_file', ],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['console', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['log_file', 'console'],
            'propagate': False,
        },
        'apps': {
            'handlers': ['log_file', ],
            'level': 'INFO',
            'propagate': True,
        },
    }
}


