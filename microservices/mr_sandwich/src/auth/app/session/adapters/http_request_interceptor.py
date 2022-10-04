from app.session.adapters.http import extract_identity, confirm_session, create_passable_request, pass_request
from app.session.domain.ports.request_interceptor import RequestInterceptor


class HttpRequestInterceptor(RequestInterceptor):
    def swallow(self, request):
        identity = extract_identity(request)
        confirm_session(identity)

        passable_request = create_passable_request(identity, request)
        response = pass_request(passable_request)

        return response
