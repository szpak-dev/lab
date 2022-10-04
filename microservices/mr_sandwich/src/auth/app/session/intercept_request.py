from flask import Request

from app.session.adapters import request_interceptor


class InterceptRequest:
    def run(self, flask_request: Request):
        return request_interceptor().swallow(flask_request)
