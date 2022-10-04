from requests import Session, Response

s = Session()


class HttpRequestPasser:
    def execute(self, prepared_request) -> Response:
        return s.send(prepared_request)


def pass_request(prepared_request) -> Response:
    return HttpRequestPasser().execute(prepared_request)
