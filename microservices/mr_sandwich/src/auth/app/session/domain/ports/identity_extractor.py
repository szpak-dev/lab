from abc import ABC, abstractmethod
from app.session.domain.models.identity import Identity


class IdentityExtractor(ABC):
    @abstractmethod
    def extract(self, request) -> Identity:
        pass
