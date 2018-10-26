"""
Email settings.
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@example.com'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = '[email_user]'
EMAIL_HOST_PASSWORD = '[email_user_password]'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
