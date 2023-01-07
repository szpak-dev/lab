from datetime import datetime

from shared.ddd import AggregateRoot
from domain.events import AuthenticationFailedEvent, AuthenticationSuccess
from domain.value_objects import Role, PlainPassword
from domain.errors import PasswordDoesNotMatch

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from shared.db import Base


class User(Base, AggregateRoot):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    roles = relationship('UserRole')

    def check_password(self, plain_password: PlainPassword) -> None:
        user_id = str(self.id)

        if plain_password.value != self.password:
            super()._emit_event(AuthenticationFailedEvent(user_id))
            raise PasswordDoesNotMatch

        super()._emit_event(AuthenticationSuccess(user_id))


class UserRole(Base):
    __tablename__ = 'user_roles'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
