from aiogram import types, Dispatcher
from tgbot.loader import bot


async def some_callback(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(some_callback,
                                       lambda call: call.data == 'some_callback_data')
