import asyncio

from adapters import user_repository
from domain.value_objects import Username, UserId


async def main():
    user = await user_repository.get_by_id(UserId('1'))
    print(user)

asyncio.run(main())
