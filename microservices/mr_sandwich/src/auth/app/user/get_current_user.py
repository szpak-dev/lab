from app.ddd.application import ApplicationCommand
from app.user.domain.entities.user import user_factory


class GetCurrentUser(ApplicationCommand):
    @staticmethod
    def run():
        return user_factory()
