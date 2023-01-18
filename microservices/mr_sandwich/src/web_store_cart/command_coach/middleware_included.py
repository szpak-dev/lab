import contextvars

from command_coach.command import Command
from command_coach.error import CommandCoachMiddlewareError
from command_coach.middleware import CommandCoachMiddleware

import logging
logger = logging.getLogger('command_coach')


class LockingMiddleware(CommandCoachMiddleware):
    current_command = contextvars.ContextVar('current_command', default='')

    async def before_handle(self, command: Command):
        current = self.current_command.get()
        logger.debug(f'LockingMiddleware.before_handle: trying to run a {command.__class__.__name__}')

        if current:
            raise CommandCoachMiddlewareError(f'LockingMiddleware is already handling a command: {current}')

        self.current_command.set(command.__class__.__name__)

    async def after_handle(self, command: Command):
        logger.debug(f'LockingMiddleware.after_handle: unlocking bus after {self.current_command.get()}')
        self.current_command.set('')


class LoggingMiddleware(CommandCoachMiddleware):
    async def before_handle(self, command: Command):
        logger.debug(f'LoggingMiddleware.before_handle: Command is about to be handled {command}')

    async def after_handle(self, command: Command):
        logger.debug(f'LoggingMiddleware.after_handle: Command {command} have been just handled')


class ExecutionTimeMiddleware(CommandCoachMiddleware):
    async def before_handle(self, command: Command):
        pass

    async def after_handle(self, command: Command):
        pass
