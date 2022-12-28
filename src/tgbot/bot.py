import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.tgbot.config import TOKEN, ROOT_DIR
from src.tgbot.handlers import errors, user, common


async def main() -> None:
    logging.basicConfig(
        style='{',
        level=logging.INFO,
        format="{asctime}: {message}",
        datefmt='%d-%B-%Y %H:%M',
        filename=f"{ROOT_DIR}/log.log",
    )

    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(errors.router)
    dp.include_router(user.router)
    dp.include_router(common.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
