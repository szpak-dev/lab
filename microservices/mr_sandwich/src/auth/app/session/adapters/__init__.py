from app.session.domain.ports.session_repository import SessionRepository
from app.session.domain.ports.jwt_repository import JwtRepository
from app.session.adapters.in_memory_session_repository import InMemorySessionRepository
from app.session.adapters.in_memory_jwt_repository import InMemoryJwtRepository
from app.session.adapters.http_api_service import HttpApiService
from app.session.adapters.http_request_interceptor import HttpRequestInterceptor
from app.session.domain.ports.api_service import ApiService
from app.session.domain.ports.request_interceptor import RequestInterceptor
from app.session.adapters.mediator_session_transceiver import MediatorSessionTransceiver
from app.mediator.event_bus import event_bus
from app.session.domain.ports.session_transceiver import SessionTransceiver

session_repository: SessionRepository = InMemorySessionRepository()
jwt_repository: JwtRepository = InMemoryJwtRepository()
request_interceptor: RequestInterceptor = HttpRequestInterceptor(session_repository, jwt_repository)
session_transceiver: SessionTransceiver = MediatorSessionTransceiver(event_bus, session_repository)

event_bus.session_transceiver = session_transceiver
api_service: ApiService = HttpApiService(session_repository, session_transceiver)
