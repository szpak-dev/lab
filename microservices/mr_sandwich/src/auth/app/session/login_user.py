from flask import make_response

from app.ddd.application import ApplicationCommand
from app.session.adapters import session_repository
from app.mediator.event_bus import bus
from app.session.domain.value_objects import Credentials


class LoginUser(ApplicationCommand):
    @staticmethod
    def run(username: str, plain_password: str):
        credentials = Credentials(username, plain_password)
        bus.session_module.emit_authorization_started(credentials)
        session = session_repository.get_for_user(username)

        response = make_response('', 201)
        response.set_cookie('session_id', session.id)
        return response
