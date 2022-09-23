from requests import Request


class PassableRequestFactory:
    @staticmethod
    def create_internet_request(flask_req):
        return Request(flask_req.method, flask_req.url, headers=flask_req.headers).prepare()

    @staticmethod
    def create_subnet_request(flask_req):
        return Request(flask_req.method, flask_req.url, headers=flask_req.headers).prepare()
