from aiogram import Bot, F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.tgbot.constants.buttons import (CALCULATE_BTN, DELETE_ALL_PERIODS_BTN,
                                         PAYMENT_TYPES_BTN,
                                         SET_ALL_PERIODS_BTN,
                                         SET_VISITING_PERIODS_BTN,
                                         START_NEW_CALCULATION_BTN, WEEKDAYS,
                                         WITH_INFRASTRUCTURE_BTN,
                                         WITHOUT_INFRASTRUCTURE_BTN,
                                         CHOOSE_All_WEEK_BTN)
from src.tgbot.constants.messages import (
    after_setting_or_deleting_periods_msg, chose_weekdays_msg,
    empty_weekdays_list_msg, get_calendar_period_msg, get_deleting_periods_msg,
    get_pay_type_msg, get_period_alert_msg, get_periods_msg,
    get_setting_period_msg, get_total_message, incorrect_period_msg,
    infrastructure_msg, unavailable_periods_kb_msg)
from src.tgbot.constants.weekdays import full_weekday_names
from src.tgbot.keyboards import inline, reply
from src.tgbot.states.user import CaringCost
from src.tgbot.tools.formatters import format_weekdays_list
from src.tgbot.tools.scripts import get_total, is_new_value_correct

router = Router()


@router.message(Command(commands=["calc"]))
@router.message(F.text == START_NEW_CALCULATION_BTN)
async def start_calc(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CaringCost.infrastructure)
    await message.answer(
        text=infrastructure_msg,
        reply_markup=reply.get_infrastructure_kb(),
    )


@router.message(F.text.in_((WITH_INFRASTRUCTURE_BTN, WITHOUT_INFRASTRUCTURE_BTN)))
async def set_infrastructure(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CaringCost.privileges)
    await state.update_data(with_infrastructure=message.text.lower())
    await message.answer(
        text=get_pay_type_msg(with_infrastructure=message.text.lower()),
        reply_markup=reply.get_client_type_kb()
    )


@router.message(CaringCost.privileges, F.text.in_(PAYMENT_TYPES_BTN))
async def set_privilege(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CaringCost.weekdays)
    await state.update_data(privilege=message.text.lower())
    await state.update_data(weekdays=[])
    await message.answer(
        text=chose_weekdays_msg,
        reply_markup=reply.get_weekdays_kb()
    )


@router.message(CaringCost.weekdays, (F.text.in_(WEEKDAYS)) | (F.text == CHOOSE_All_WEEK_BTN))
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


@router.message(CaringCost.weekdays, F.text == CALCULATE_BTN)
async def calculate(message: types.Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    if user_data.get('weekdays'):
        await message.answer(
            text=get_total_message(data=get_total(user_data)),
            reply_markup=reply.get_new_calc_kb(),
        )
        await state.set_state(None)
    else:
        await message.answer(
            text=empty_weekdays_list_msg,
            reply_markup=reply.get_weekdays_kb(),
        )


@router.message(Command(commands=["date"]))
@router.message(F.text == SET_VISITING_PERIODS_BTN)
async def set_period(message: types.Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    await state.set_state(CaringCost.period)
    periods = user_data.get('periods')

    if not periods:
        await state.update_data(periods=[])

    calendar_kb_msg_id = await message.answer(
        text='Выберите один или несколько периодов посещений используя кнопки '
             'c нужным числом под этим сообщением: 👇🏻',
        reply_markup=inline.get_calendar_kb()
    )
    await state.update_data(calendar_kb_msg_id=calendar_kb_msg_id.message_id)
    msg = await message.answer(text=f"{get_calendar_period_msg(periods=periods)}\n",
                               reply_markup=reply.get_cancel_period_kb())
    await state.update_data(msg_id=msg.message_id)


async def update_periods_msg(message: types.Message, periods: list):
    await message.edit_text(
        text=get_periods_msg(periods=periods),
        reply_markup=inline.get_calendar_kb()
    )


@router.callback_query()
async def callbacks_periods(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    tmp_data = await state.get_data()
    periods = tmp_data.get('periods')

    if periods is None:
        await callback.answer(text=unavailable_periods_kb_msg, show_alert=True)
        await bot.send_message(text=after_setting_or_deleting_periods_msg,
                               chat_id=callback.from_user.id,
                               reply_markup=reply.get_new_calc_kb())
    else:
        callback_data = callback.data
        tmp_data = await state.get_data()
        period_ind = tmp_data.get('period_ind', 0)

        if callback_data == 'ignore':
            await callback.answer(text="Выберите число месяца!", show_alert=True)
        else:
            if [] not in periods:
                periods.append([])
            period_len = len(periods[period_ind])
            if is_new_value_correct(periods=periods, new_value=int(callback_data)):
                if period_len == 0:
                    periods[period_ind].append(int(callback_data))
                    await callback.answer(text=get_period_alert_msg(is_start_period=True,
                                                                    callback_data=callback_data), show_alert=True)
                elif period_len == 1:
                    periods[period_ind].append(int(callback_data))
                    await callback.answer(text=get_period_alert_msg(is_start_period=False,
                                                                    callback_data=callback_data), show_alert=True)
                    period_ind += 1
                    tmp_data['period_ind'] = period_ind
                    await update_periods_msg(callback.message, periods)
            else:
                await callback.answer(text=incorrect_period_msg, show_alert=True)
            await state.update_data(tmp_data)
    await callback.answer()


@router.message(CaringCost.period, F.text == SET_ALL_PERIODS_BTN)
async def set_periods(message: types.Message, state: FSMContext, bot: Bot) -> None:
    data = await state.get_data()
    await bot.delete_message(chat_id=message.chat.id, message_id=data['calendar_kb_msg_id'])
    await state.set_state(CaringCost.infrastructure)
    periods = data.get('periods')
    await message.answer(
        text=get_setting_period_msg(periods=periods),
        reply_markup=reply.get_new_calc_kb()
    )


@router.message(CaringCost.period, F.text == DELETE_ALL_PERIODS_BTN)
async def delete_periods(message: types.Message, state: FSMContext, bot: Bot) -> None:
    data = await state.get_data()
    await bot.delete_message(chat_id=message.chat.id, message_id=data['calendar_kb_msg_id'])
    await state.set_state(CaringCost.infrastructure)
    periods = data.pop('periods')
    if data.get('period_ind') is not None:
        del data['period_ind']
    await state.set_data(data=data)
    await message.answer(
        text=get_deleting_periods_msg(periods=periods),
        reply_markup=reply.get_new_calc_kb()
    )
