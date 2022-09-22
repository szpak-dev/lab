import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/food_factory/hello')
    def hello():
        return 'Hello world'

    return app
