from users.domain.ports.api_service import ApiService
from users.domain.ports.user_repository import UserRepository


class HttpApiService(ApiService):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_user(self, username: str):
        return self._user_repository.get_by_username(username)
