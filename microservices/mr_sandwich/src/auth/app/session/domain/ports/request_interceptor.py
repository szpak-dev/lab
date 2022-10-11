from abc import ABC, abstractmethod


class RequestInterceptor(ABC):
    @abstractmethod
    def pass_request(self, request):
        pass
