from flask import Flask, request, abort

from cli import add_user
from sessions.adapters import api_service
from sessions.domain.errors import SessionError
from sessions.ui.login import login_action, Credentials
from sessions.ui.logout import logout_action
from sessions.ui.proxy_pass import proxy_pass_action
from users.domain.errors import UserError
from users.ui.get_user import get_user_action

allowed_http_methods = ['GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.cli.add_command(add_user)

    @app.route('/auth/login', methods=['POST'])
    def login():
        try:
            return login_action(Credentials(
                username=request.form.get('username'),
                password=request.form.get('password')
            ))
        except (UserError, SessionError):
            abort(401)

    @app.route('/auth/logout')
    def logout():
        try:
            return logout_action(request.cookies.get('session_id'))
        except (UserError, SessionError):
            abort(401)

    @app.route('/auth/users')
    def me():
        try:
            username = api_service.get_current_username(request.cookies.get('session_id'))
            return get_user_action(username)
        except (UserError, SessionError):
            abort(401)

    @app.route('/<string:path>', defaults={'path': ''}, methods=allowed_http_methods)
    @app.route('/<string:path>', methods=allowed_http_methods)
    @app.route('/<path:path>', methods=allowed_http_methods)
    def proxy_pass(path):
        try:
            return proxy_pass_action(request)
        except SessionError:
            abort(401)

    return app
