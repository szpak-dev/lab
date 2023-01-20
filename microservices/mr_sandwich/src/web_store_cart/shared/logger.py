import logging

from os import getenv
from logging.config import dictConfig


_WSGI_LOG_LEVEL = getenv('WSGI_LOG_LEVEL', 'NO_WSGI')
_APP_LOG_LEVEL = getenv('APP_LOG_LEVEL', 'DEBUG')

dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': _APP_LOG_LEVEL,
    },
    'command_coach': {
        'handlers': ['console'],
        'level': _APP_LOG_LEVEL,
    },
})


logging = logging
