from flask import make_response
from app.session.adapters import session_repository
from app.shared import ApplicationCommand


class LoginUser(ApplicationCommand):
    @staticmethod
    def run(username: str, plain_password: str):
        session = session_repository().get_for_user(username)

        response = make_response('', 201)
        response.set_cookie('session_id', session.id)
        return response
