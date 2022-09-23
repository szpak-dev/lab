from app.user.domain.models.role import Role
from app.user.domain.models.username import Username


class User:
    def __init__(self, username: Username, role: Role):
        self.username = username
        self.role = role
