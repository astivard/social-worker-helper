from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.tgbot.keyboards import reply
from src.tgbot.services.data import available_privileges, available_weekdays
from src.tgbot.services.messages import (get_help_msg, get_reboot_msg,
                                         get_tariffs_msg, get_welcome_msg)

router = Router()


@router.message(Command(commands=["help"]))
async def help_cmd(message: types.Message, state: FSMContext) -> None:
    await state.set_state(state=None)
    await message.answer(
        text=get_help_msg(),
        reply_markup=reply.get_new_calc_kb(),
    )


@router.message(Command(commands=["start"]))
async def start_cmd(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        text=get_welcome_msg(),
        reply_markup=reply.get_new_calc_kb(),
    )


@router.message(Command(commands=["tariffs"]))
async def tariffs_cmd(message: types.Message, state: FSMContext) -> None:
    await state.set_state(state=None)
    await message.answer(
        text=get_tariffs_msg(),
        reply_markup=reply.get_new_calc_kb(),
    )


@router.message((F.text.lower().in_(available_privileges)) |
                ((F.text.lower().in_(available_weekdays)) |
                (F.text.lower() == 'выбрать всю неделю')) |
                (F.text.lower() == 'рассчитать') |
                (F.text.lower() == 'считать за весь месяц'))
async def else_cmd(message: types.Message) -> None:
    await message.answer(
        text=get_reboot_msg(),
        reply_markup=reply.get_new_calc_kb(),
    )
