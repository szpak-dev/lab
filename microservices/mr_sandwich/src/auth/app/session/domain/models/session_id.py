from random import randrange
from typing import TypeVar

T = TypeVar('T', bound='SessionId')


class SessionId:
    def __init__(self, session_id: str):
        self.id = session_id

    @staticmethod
    def generate(length: int = 20) -> T:
        chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        steps = range(0, length)

        num = []
        for step in steps:
            character_index = randrange(0, len(chars) - 1)
            num.append(chars[character_index])

        number = ''.join(num)
        return SessionId(number)
