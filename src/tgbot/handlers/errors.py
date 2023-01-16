from aiogram import Bot, F, Router, types
from aiogram.fsm.context import FSMContext

from src.tgbot.config import ADMIN_ID
from src.tgbot.constants.buttons import FOR_REBOOT_BUTTONS
from src.tgbot.constants.messages import (get_incorrect_msg_from_user,
                                          help_msg, reboot_msg)
from src.tgbot.keyboards import reply

router = Router()


@router.message(F.text.in_(FOR_REBOOT_BUTTONS))
async def else_cmd(message: types.Message, state: FSMContext) -> None:
    await state.clear()
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