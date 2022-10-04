from abc import ABC, abstractmethod


class RequestInterceptor(ABC):
    @abstractmethod
    def swallow(self, request):
        pass
