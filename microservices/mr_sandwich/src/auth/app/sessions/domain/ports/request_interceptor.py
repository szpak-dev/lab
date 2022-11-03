from abc import ABC, abstractmethod
from flask import Request
from requests import Response


class RequestInterceptor(ABC):
    @abstractmethod
    def pass_request(self, flask_request: Request) -> Response:
        pass
