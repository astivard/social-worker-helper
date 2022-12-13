import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN

from tgbot.handlers import user


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(user.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
