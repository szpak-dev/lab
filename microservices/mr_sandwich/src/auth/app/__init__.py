from flask import Flask, request, abort, make_response

from app.session.adapters.http.interceptor import Interceptor

interceptor = Interceptor()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/auth/login')
    def login():
        response = make_response('ok', 200)
        response.set_cookie('session_id', 'session123456')
        return response

    @app.route('/', defaults={'path': ''})
    @app.route('/<string:path>')
    @app.route('/<path:path>')
    def hello(path):
        try:
            response = interceptor.swallow(request)

            if response.status_code == 200:
                return make_response(response.text, 200)

            abort(response.status_code)
        except RuntimeError:
            abort(401)

    return app
