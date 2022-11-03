from flask import Response, make_response
from sessions.adapters import api_service


def logout_action(session_id: str) -> Response:
    username = api_service.get_current_username(session_id)
    api_service.destroy_session(username)

    response = make_response('', 204)
    response.delete_cookie('session_id')
    return response
