from aiogram import F, Router, types

from src.tgbot.states.user import CaringCost
from src.tgbot.tools.month import get_available_month_days_numbers

router = Router()


@router.message(CaringCost.from_date,
                ~F.text.in_(get_available_month_days_numbers()) &
                ~F.text.lower().in_(('считать за весь месяц', '/start', '/calc',
                                     '/help', '/date', '/tariffs', '/holidays')))
async def any_digits_handler(message: types.Message):
    await message.answer(
        text='❗️Вы ввели неверное число месяца, попробуйте ещё раз: 👇🏻',
    )
