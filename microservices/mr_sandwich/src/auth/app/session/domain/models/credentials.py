from app.user.domain.models.password import Password
from app.user.domain.models.username import Username


class Credentials:
    def __init__(self, username: Username, password: Password):
        self.username = username
        self.password = password
