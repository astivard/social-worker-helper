from aiogram import types, Dispatcher


async def send_welcome_message(message: types.Message):
    await message.answer('Hi~!')


def setup(dp: Dispatcher):
    # dp.register_message_handler(send_welcome_message,
    #                             content_types=('text',),
    #                             state='*',
    #                             commands=('start',))
    dp.register_message_handler(send_welcome_message)
