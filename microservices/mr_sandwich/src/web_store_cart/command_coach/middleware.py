from abc import ABC, abstractmethod
from typing import List

from command_coach.command import Command


class CommandCoachMiddleware(ABC):
    @abstractmethod
    async def before_handle(self, command: Command):
        pass

    @abstractmethod
    async def after_handle(self, command: Command):
        pass


class Middleware:
    def __init__(self, found: List[CommandCoachMiddleware] = []):
        self.found = found

    def __call__(self, *args, **kwargs):
        self.found.append(args[0]())

    async def before(self, command: Command):
        for m in self.found:
            await m.before_handle(command)

    async def after(self, command: Command):
        for m in self.found:
            await m.after_handle(command)
