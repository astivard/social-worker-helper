from aiogram import executor

from handlers import message
from loader import dp

if __name__ == '__main__':
    message.setup(dp)
    executor.start_polling(dp, skip_updates=True)
