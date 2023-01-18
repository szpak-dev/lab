from importlib import import_module
from typing import List

from command_coach.command import Command, CommandHandler
from command_coach.error import CommandCoachError
from command_coach.middleware import Middleware, CommandCoachMiddleware


def _instantiate_handler_for_command(command: Command):
    command_class_name = command.__class__.__name__
    module = import_module(command.__module__)

    handler_class = getattr(module, f'{command_class_name}Handler')
    if not issubclass(handler_class, CommandHandler):
        raise CommandCoachError('Command Handler must inherit directly from <CommandHandler>')

    return handler_class()


class CommandCoach:
    def __init__(self, from_included: List[CommandCoachMiddleware]):
        self._from_included = from_included

    async def handle(self, command: Command) -> None:
        m = Middleware(self._from_included)

        if not isinstance(command, Command):
            raise CommandCoachError('Every command must be a child of <Command> class')

        handler = _instantiate_handler_for_command(command)

        await m.before(command)
        await handler.handle(command)
        await m.after(command)
