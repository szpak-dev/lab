import logging

from os import getenv
from logging.config import dictConfig

_WSGI_LOG_LEVEL = getenv('WSGI_LOG_LEVEL', 'NO_WSGI')
_APP_LOG_LEVEL = getenv('APP_LOG_LEVEL', 'WARNING')

dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'app': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'formatter': 'app',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': _APP_LOG_LEVEL,
    },
})

logging.info('Container logging, WSGI: {}, App: {}'.format(
    _WSGI_LOG_LEVEL,
    _APP_LOG_LEVEL,
))

logging = logging
