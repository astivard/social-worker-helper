from aiogram import F, Router, types

from src.tgbot.services.data import available_month_days_numbers
from src.tgbot.states.user import CaringCost

router = Router()


@router.message(CaringCost.from_date,
                ~F.text.in_(available_month_days_numbers) &
                ~F.text.lower().in_(('считать за весь месяц', '/start', '/calc', '/help', '/date', '/tariffs')))
async def any_digits_handler(message: types.Message):
    await message.answer(
        text='❗️Вы ввели неверное число месяца, попробуйте ещё раз: 👇🏻',
    )
