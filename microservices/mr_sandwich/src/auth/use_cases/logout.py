from fastapi import Request, Response, HTTPException
from adapters import session_repository
from domain.errors import IdentityNotFound
from domain.services import extract_session_id


def logout_action(request: Request, response: Response):
    try:
        session_id = extract_session_id(request)
        session_repository.destroy_session(session_id)
        response.delete_cookie('session_id')
        response.headers['Authorization'] = ''
    except IdentityNotFound:
        raise HTTPException(status_code=409, detail='No Identity found, no need to logout')
