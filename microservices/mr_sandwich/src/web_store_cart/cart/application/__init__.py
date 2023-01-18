from command_coach.command_bus import CommandCoach
from command_coach.middleware_included import LockingMiddleware, LoggingMiddleware

command_bus = CommandCoach([
    LockingMiddleware(),
    LoggingMiddleware(),
])
