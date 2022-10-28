from os import getenv

_WSGI_LOG_LEVEL = getenv('WSGI_LOG_LEVEL', 'NO_WSGI')
_DJANGO_LOG_LEVEL = getenv('DJANGO_LOG_LEVEL', 'WARNING')

MY_LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': _DJANGO_LOG_LEVEL,
    },
}

print('Container logging, WSGI: {}, Django: {}'.format(
    _WSGI_LOG_LEVEL,
    _DJANGO_LOG_LEVEL,
), flush=True)
