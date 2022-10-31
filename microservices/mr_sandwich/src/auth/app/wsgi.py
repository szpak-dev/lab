from flask_app import create_app
from logger import logging

logging.info('Starting auth application...')
app = create_app()
