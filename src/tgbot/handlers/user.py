from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.tgbot.keyboards import reply
from src.tgbot.services.services import format_weekdays_list, get_total
from src.tgbot.states.user import CaringCost

router = Router()

available_privileges = ('да', 'нет')
available_weekdays = ('пн', 'вт', 'ср', 'чт', 'пт')


@router.message(Command(commands=["start"]))
@router.message(F.text.lower().casefold() == 'начать новый расчет')
async def start_calc(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(CaringCost.privileges)
    await message.answer(
        text="Выберите, является ли пожилой льготником: 👇🏻",
        reply_markup=reply.get_yes_no_kb(),
    )


@router.message(CaringCost.privileges, F.text.lower().in_(available_privileges))
async def set_privilege(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CaringCost.weekdays)
    await state.update_data(privilege=message.text.lower())
    await state.update_data(weekdays=[])
    await message.answer(
        text="Выберите дни недели, в которые обслуживается пожилой, затем нажмите рассчитать: 👇🏻",
        reply_markup=reply.get_weekdays_kb()
    )


@router.message(CaringCost.weekdays, F.text.lower().in_(available_weekdays))
async def set_weekdays(message: types.Message, state: FSMContext) -> None:
    weekday = message.text.lower()
    tmp_data = await state.get_data()
    if weekday not in tmp_data['weekdays']:
        tmp_data['weekdays'].append(weekday)
    await state.update_data(tmp_data)

    user_data = await state.get_data()
    await message.answer(text=f"Вы выбрали дни недели:\n\n{format_weekdays_list(user_data['weekdays'])}")


@router.message(CaringCost.weekdays, F.text.lower().casefold() == 'рассчитать')
async def calculate(message: types.Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    await state.clear()
    await message.answer(
        text=get_total(user_data),
        reply_markup=reply.get_new_calc_kb(),
    )
