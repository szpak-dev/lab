from flask import Request

from app.session.domain.value_objects import Identity


class PassableRequestFactory:
    @staticmethod
    def create_internet_request(flask_req):
        return Request(flask_req.method, flask_req.url, headers=flask_req.headers).prepare()

    @staticmethod
    def create_subnet_request(flask_req):
        return Request(flask_req.method, flask_req.url, headers=flask_req.headers).prepare()


def create_passable_request(identity: Identity, flask_request: Request):
    if identity.requested_from_internet():
        return PassableRequestFactory().create_internet_request(flask_request)
    elif identity.requested_from_subnet():
        return PassableRequestFactory().create_subnet_request(flask_request)