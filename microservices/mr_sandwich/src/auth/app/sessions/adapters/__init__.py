from sessions.domain.ports.session_repository import SessionRepository
from sessions.domain.ports.jwt_repository import JwtRepository
from sessions.adapters.in_memory_session_repository import InMemorySessionRepository
from sessions.adapters.in_memory_jwt_repository import InMemoryJwtRepository
from sessions.adapters.http_api_service import HttpApiService
from sessions.adapters.http_request_interceptor import HttpRequestInterceptor
from sessions.domain.ports.api_service import ApiService
from sessions.domain.ports.request_interceptor import RequestInterceptor
from sessions.adapters.mediator_session_transceiver import MediatorSessionTransceiver
from mediator.event_bus import event_bus
from sessions.domain.ports.session_transceiver import SessionTransceiver

session_repository: SessionRepository = InMemorySessionRepository()
jwt_repository: JwtRepository = InMemoryJwtRepository()
request_interceptor: RequestInterceptor = HttpRequestInterceptor(session_repository, jwt_repository)
session_transceiver: SessionTransceiver = MediatorSessionTransceiver(event_bus, session_repository)

event_bus.session_transceiver = session_transceiver
api_service: ApiService = HttpApiService(session_repository, session_transceiver)
