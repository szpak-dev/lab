from abc import ABC, abstractmethod


class ApiService(ABC):
    @abstractmethod
    def create_session(self, username: str, password: str):
        pass

    @abstractmethod
    def destroy_session(self, username: str):
        pass

    @abstractmethod
    def get_current_username(self, raw_session_id: str):
        pass
