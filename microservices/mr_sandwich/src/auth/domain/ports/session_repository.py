from abc import ABC, abstractmethod

from domain.value_objects import Username


class SessionRepository(ABC):
    @abstractmethod
    def create_session(self, username: Username):
        pass

    @abstractmethod
    def destroy_session(self, username: Username):
        pass

    @abstractmethod
    def get_current_username(self, raw_session_id: str):
        pass
