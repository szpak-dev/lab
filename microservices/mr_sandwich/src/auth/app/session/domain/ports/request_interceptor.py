from abc import ABC, abstractmethod
from flask_app import Request as FlaskRequest
from requests import Response


class RequestInterceptor(ABC):
    @abstractmethod
    def pass_request(self, flask_request: FlaskRequest) -> Response:
        pass
