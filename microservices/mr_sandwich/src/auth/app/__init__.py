from flask import Flask, request, abort, make_response

from app.session.domain.errors import SessionError
from app.cli import add_user
from app.session.adapters import api_service, request_interceptor

# tight coupling with user aggregate
from app.user.adapters import user_repository
from app.user.domain.errors import UserError


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.cli.add_command(add_user)

    @app.route('/auth/login')
    def login():
        try:
            session = api_service.create_session('admin_user', 'password')

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

            view = {"id": user.id.id, "username": user.username.value}
            return make_response(view, 200)
        except (UserError, SessionError) as e:
            print(e, flush=True)
            abort(401)

    @app.route('/', defaults={'path': ''})
    @app.route('/<string:path>')
    @app.route('/<path:path>')
    def proxy_pass(path):
        try:
            return request_interceptor.pass_request(request)
        except SessionError:
            abort(401)

    return app
