from flask import Request

from app.session.adapters.db.in_memory_session_repository import InMemorySessionRepository
from app.session.adapters.http.jwt_manager import JwtManager
from app.session.adapters.http.passable_request_factory import PassableRequestFactory
from app.session.adapters.http.request_identity_extractor import RequestIdentityExtractor
from app.session.adapters.http.request_passer import RequestPasser

request_identity_checker = RequestIdentityExtractor()
session_repository = InMemorySessionRepository()
request_passer = RequestPasser()
factory = PassableRequestFactory()
jwt_manager = JwtManager()


class Interceptor:
    @staticmethod
    def swallow(flask_request: Request):
        identity = request_identity_checker.extract(flask_request)

        if identity.requested_from_subnet():
            jwt_manager.validate(identity.value())
            passable_request = factory.create_subnet_request(flask_request)
            return request_passer.pass_request(passable_request)

        if identity.requested_from_internet():
            session = session_repository.get(identity.value())

            if session:
                passable_request = factory.create_internet_request(flask_request)
                return request_passer.pass_request(passable_request)

        raise RuntimeError('Session not found')
