from requests import Session, Response
from flask import Request

s = Session()


class RequestPasser:
    @staticmethod
    def pass_request(prepared_request) -> Response:
        return s.send(prepared_request)
