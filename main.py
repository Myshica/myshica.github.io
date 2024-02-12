import asyncio
import logging
import sys

from app import *
from handlers import start_router

ROUTERS = [
    start_router
]


async def start_routers():
    for i in ROUTERS:
        dp.include_router(i)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await start_routers()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
