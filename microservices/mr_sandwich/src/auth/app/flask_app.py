from flask import Flask, request, abort, make_response

from sessions.domain.errors import SessionError
from sessions.adapters import api_service, request_interceptor
from cli import add_user

# tight coupling with users aggregate
from users.adapters import user_repository
from users.domain.errors import UserError

allowed_http_methods = ['GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.cli.add_command(add_user)

    @app.route('/auth/login', methods=['POST'])
    def login():
        try:
            session = api_service.create_session(
                request.form.get('username'),
                request.form.get('password'),
            )

            response = make_response('', 201)
            response.set_cookie('session_id', session.raw_id())
            return response
        except (UserError, SessionError):
            abort(401)

    @app.route('/auth/logout')
    def logout():
        try:
            api_service.destroy_session('admin_user')

            response = make_response('', 204)
            response.delete_cookie('session_id')
            return response
        except (UserError, SessionError):
            abort(401)

    @app.route('/auth/users')
    def me():
        try:
            username = api_service.get_current_username(request.cookies.get('session_id'))
            user = user_repository.get_by_username(username)

            return make_response(user.serialize(), 200)
        except (UserError, SessionError):
            abort(401)

    @app.route('/<string:path>', defaults={'path': ''}, methods=allowed_http_methods)
    @app.route('/<string:path>', methods=allowed_http_methods)
    @app.route('/<path:path>', methods=allowed_http_methods)
    def proxy_pass(path):
        app.logger.info(request)
        try:
            res = request_interceptor.pass_request(request)
            text, headers, status_code = res.text, dict(res.headers), res.status_code

            flask_response = make_response(text, status_code, headers)
            flask_response.headers = headers

            return flask_response
        except SessionError:
            abort(401)

    return app
