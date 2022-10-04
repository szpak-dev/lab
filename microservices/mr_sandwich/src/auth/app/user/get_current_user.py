from app.shared import ApplicationCommand
from app.user.domain.entities.user import create_user


class GetCurrentUser(ApplicationCommand):
    @staticmethod
    def run():
        return create_user()
