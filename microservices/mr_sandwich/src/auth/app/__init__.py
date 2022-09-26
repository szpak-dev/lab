from flask import Flask, request, abort, make_response

from app.session.adapters.http.interceptor import Interceptor
from app.user.adapters.db.in_memory_user_authenticator import InMemoryUserAuthenticator

interceptor = Interceptor()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/auth/login')
    def login():
        session_id = InMemoryUserAuthenticator().check_credentials('test_user', 'password')
        response = make_response('', 201)
        response.set_cookie('session_id', session_id.id)
        return response

    @app.route('/auth/logout')
    def logout():
        response = make_response('', 204)
        response.delete_cookie('session_id')
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
