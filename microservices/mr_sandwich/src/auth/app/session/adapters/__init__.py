from app.session.domain.ports.session_repository import SessionRepository
from app.session.domain.ports.request_interceptor import RequestInterceptor
from app.session.adapters.http_request_interceptor import HttpRequestInterceptor
from app.session.adapters.in_memory_session_repository import InMemorySessionRepository


def request_interceptor() -> RequestInterceptor:
    return HttpRequestInterceptor()


def session_repository() -> SessionRepository:
    return InMemorySessionRepository()
