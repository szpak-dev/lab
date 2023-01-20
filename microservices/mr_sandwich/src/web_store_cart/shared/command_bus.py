from __future__ import annotations

from command_coach.adapter import AsyncDatabase
from command_coach.bus import command_bus_maker
from command_coach.plugin_included import LockingPlugin, TransactionPluginAsync

from shared.db import database, Database


class DatabaseAdapter(AsyncDatabase):
    def __init__(self, db: Database):
        self._session = db.current_session()

    async def begin_transaction(self):
        await self._session.begin()

    async def commit_transaction(self):
        await self._session.commit()

    async def rollback_transaction(self):
        await self._session.rollback()


bus = command_bus_maker([
    LockingPlugin(),
    TransactionPluginAsync(DatabaseAdapter(database)),
])
