import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.tgbot.config import TOKEN, ROOT_DIR
from src.tgbot.handlers import errors, user


async def main() -> None:
    logging.basicConfig(
        style='{',
        level=logging.WARNING,
        format="{asctime}: {message}",
        datefmt='%d-%B-%Y %H:%M',
        filename=f"{ROOT_DIR}/log.log",
        filemode='w',
    )

    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(errors.router)
    dp.include_router(user.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
