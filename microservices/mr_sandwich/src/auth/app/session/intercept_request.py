from flask import Request

from app.shared import ApplicationCommand
from app.session.adapters.http.request_identity_extractor import extract_identity
from app.session.domain.services import assert_valid_identity
from app.session.adapters.http.passable_request_factory import create_passable_request
from app.session.adapters.http.request_passer import pass_request


class InterceptRequest(ApplicationCommand):
    @staticmethod
    def run(flask_request: Request):
        identity = extract_identity(flask_request)
        assert_valid_identity(identity)

        passable_request = create_passable_request(identity, flask_request)
        response = pass_request(passable_request)

        return response
