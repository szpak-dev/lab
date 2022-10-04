from requests import Session, Response

s = Session()


class HttpRequestPasser:
    def execute(self, prepared_request) -> Response:
        return s.send(prepared_request)
