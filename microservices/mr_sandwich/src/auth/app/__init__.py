from flask import Flask, request, abort, make_response

from app.session.intercept_request import InterceptRequest
from app.session.login_user import LoginUser
from app.session.logout_user import LogoutUser


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/auth/login')
    def login():
        return LoginUser().run('test_user', 'encoded')

    @app.route('/auth/logout')
    def logout():
        return LogoutUser().run('user-id')

    @app.route('/users/me')
    def me():
        response = make_response({"id": "test", "username": "test-user", "role": "SUPER_ADMIN"}, 200)
        return response

    @app.route('/', defaults={'path': ''})
    @app.route('/<string:path>')
    @app.route('/<path:path>')
    def hello(path):
        return InterceptRequest().run(request)

    return app
