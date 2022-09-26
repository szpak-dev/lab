from app.user.domain.models.role import Role
from app.user.domain.models.username import Username
from app.user.domain.models.user_id import UserId


class User:
    def __init__(self, user_id: UserId, username: Username, role: Role):
        self.id = user_id
        self.username = username
        self.role = role
