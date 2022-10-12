from flask import Request as FlaskRequest
from requests import Request

from app.session.domain.value_objects import Identity


def create_passable_request(identity: Identity, flask_request: FlaskRequest):
    if identity.requested_from_internet():
        return Request(
            method=flask_request.method,
            url=flask_request.url,
            headers=flask_request.headers
        ).prepare()
    elif identity.requested_from_subnet():
        return Request(
            method=flask_request.method,
            url=flask_request.url,
            headers=flask_request.headers
        ).prepare()
