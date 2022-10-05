from flask import Flask, request, abort, make_response

from app.session.intercept_request import InterceptRequest
from app.session.login_user import LoginUser
from app.session.logout_user import LogoutUser
from app.user.get_current_user import GetCurrentUser
from app.session.domain.errors import IdentityNotFound, SessionNotFound
from app.cli import add_user


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.cli.add_command(add_user)

    @app.route('/auth/login')
    def login():
        return LoginUser().run('user_admin', 'password')

    @app.route('/auth/logout')
    def logout():
        return LogoutUser().run('user-id')

    @app.route('/users/me')
    def me():
        return GetCurrentUser().run()

    @app.route('/', defaults={'path': ''})
    @app.route('/<string:path>')
    @app.route('/<path:path>')
    def hello(path):
        try:
            return InterceptRequest().run(request)
        except (IdentityNotFound, SessionNotFound):
            abort(401)

    return app
