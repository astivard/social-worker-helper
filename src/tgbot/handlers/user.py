from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.tgbot.constants.buttons import *
from src.tgbot.constants.messages import (get_from_date_message,
                                          get_total_message,
                                          privileges_message)
from src.tgbot.keyboards import reply
from src.tgbot.states.user import CaringCost
from src.tgbot.tools.formatters import format_weekdays_list
from src.tgbot.tools.month import get_available_month_days_numbers
from src.tgbot.tools.scripts import get_total

router = Router()


@router.message(Command(commands=["calc"]))
@router.message((F.text.lower() == 'начать новый расчет') |
                (F.text.in_(get_available_month_days_numbers())))
async def start_calc(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CaringCost.privileges)

    if message.text in get_available_month_days_numbers():
        await message.answer(
            text=get_from_date_message(msg=message.text)
        )
        await state.update_data(from_date=message.text)
    await message.answer(
        text=privileges_message,
        reply_markup=reply.get_yes_no_kb(),
    )


@router.message(CaringCost.privileges, F.text.lower().in_(('да', 'нет')))
async def set_privilege(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CaringCost.weekdays)
    await state.update_data(privilege=message.text.lower())
    await state.update_data(weekdays=[])
    await message.answer(
        text="Выберите дни недели (либо всю неделю целиком), в которые обслуживается клиент, "
             "затем нажмите рассчитать: 👇🏻",
        reply_markup=reply.get_weekdays_kb()
    )


@router.message(CaringCost.weekdays,
                (F.text.lower().in_(full_weekday_names.keys())) |
                (F.text.lower() == 'выбрать всю неделю'))
async def set_weekdays(message: types.Message, state: FSMContext) -> None:
    msg = message.text.lower()
    tmp_data = await state.get_data()
    data = tmp_data['weekdays']

    if msg == 'выбрать всю неделю':
        weekdays_to_extend = list(set(full_weekday_names.keys()) - set(data))
        data.extend(weekdays_to_extend)
    elif msg not in data:
        data.append(msg)

    await state.update_data(tmp_data)

    user_data = await state.get_data()
    await message.answer(text=f"Вы выбрали дни недели:\n\n{format_weekdays_list(user_data['weekdays'])}")


@router.message(CaringCost.weekdays, F.text.lower() == 'рассчитать')
async def calculate(message: types.Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    from_date = user_data.get('from_date')

    if from_date in ('1', None):
        await state.clear()
    else:
        await state.set_state(state=None)
        await state.set_data({'from_date': from_date})

    await message.answer(
        text=get_total_message(data=get_total(user_data)),
        reply_markup=reply.get_new_calc_kb(),
    )


@router.message(Command(commands=["date"]))
@router.message(F.text.lower() == SET_VISITING_PERIOD_BTN)
async def set_from_date(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CaringCost.from_date)
    await message.answer(
        text='Пожалуйста, введите число текущего месяца, с которого хотите проводить расчеты: 👇🏻'
             '\n\n⚠️ Для отмены даты отсчета нажмите <b>Считать за весь месяц</b>',
        reply_markup=reply.get_cancel_from_date_kb()
    )


@router.message(CaringCost.from_date, F.text.lower() == 'считать за весь месяц')
async def cansel_from_date(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CaringCost.privileges)
    await state.update_data(from_date='1')
    await message.answer(
        text='⚠️Вы успешно отменили дату отсчета.\n'
             'Все последующие расчеты будут проводиться с <b>начала</b> месяца.\n\n'
             f'{privileges_message}',
        reply_markup=reply.get_yes_no_kb()
    )
