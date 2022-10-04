from flask import make_response

from app.session.adapters import session_repository
from app.shared import ApplicationCommand


class LogoutUser(ApplicationCommand):
    @staticmethod
    def run(username: str):
        session = session_repository().get_for_user(username)
        if session:
            session_repository().remove(session.id)

        response = make_response('', 204)
        response.delete_cookie('session_id')

        return response
