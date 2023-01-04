from aiogram import F, Router, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.tgbot.config import ADMIN_ID
from src.tgbot.keyboards import reply
from src.tgbot.services.data import available_privileges, available_weekdays
from src.tgbot.services.messages import (help_msg, reboot_msg,
                                         tariffs_msg, welcome_msg, get_new_user_msg, get_incorrect_msg_from_user)

router = Router()


@router.message(Command(commands=["help"]))
async def help_cmd(message: types.Message, state: FSMContext) -> None:
    await state.set_state(state=None)
    await message.answer(
        text=help_msg,
        reply_markup=reply.get_new_calc_kb(),
    )


@router.message(Command(commands=["start"]))
async def start_cmd(message: types.Message, state: FSMContext, bot: Bot) -> None:
    await state.clear()
    await message.answer(
        text=welcome_msg,
        reply_markup=reply.get_new_calc_kb(),
    )
    fullname = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id

    await bot.send_message(chat_id=ADMIN_ID, text=get_new_user_msg(fullname=fullname,
                                                                   username=username,
                                                                   user_id=user_id))


@router.message(Command(commands=["tariffs"]))
async def tariffs_cmd(message: types.Message, state: FSMContext) -> None:
    await state.set_state(state=None)
    await message.answer(
        text=tariffs_msg,
        reply_markup=reply.get_new_calc_kb(),
    )


@router.message((F.text.lower().in_(available_privileges)) |
                ((F.text.lower().in_(available_weekdays)) |
                 (F.text.lower() == 'выбрать всю неделю')) |
                (F.text.lower() == 'рассчитать') |
                (F.text.lower() == 'считать за весь месяц'))
async def else_cmd(message: types.Message) -> None:
    await message.answer(
        text=reboot_msg,
        reply_markup=reply.get_new_calc_kb(),
    )


@router.message()
async def any_cmd(message: types.Message, state: FSMContext, bot: Bot) -> None:
    await state.set_state(state=None)
    await message.answer(
        text=help_msg,
        reply_markup=reply.get_new_calc_kb(),
    )
    username = message.from_user.username
    user_id = message.from_user.id
    await bot.send_message(chat_id=ADMIN_ID, text=get_incorrect_msg_from_user(username=username,
                                                                              user_id=user_id,
                                                                              msg=message.text))
