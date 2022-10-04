from flask import make_response
from app.hooks import on_authentication_started


class LoginUser:
    def run(self, username: str, plain_password: str):
        on_authentication_started(username, plain_password)

        response = make_response('', 201)
        response.set_cookie('session_id', 'session-id')
        return response
