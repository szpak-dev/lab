from requests import Session, Response

s = Session()


def pass_request(prepared_request) -> Response:
    return s.send(prepared_request)
