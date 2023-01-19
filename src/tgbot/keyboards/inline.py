import calendar

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.tgbot.constants.buttons import ALL_WEEKDAYS
from src.tgbot.tools.month import get_current_month_and_year_number, get_current_month_name

month, year = get_current_month_and_year_number()


def get_calendar_kb() -> InlineKeyboardMarkup:
    month_calendar = calendar.monthcalendar(year, month)
    keyboard = [[
        InlineKeyboardButton(
            text=f'{get_current_month_name(case=1).title()} {str(year)}',
            callback_data='ignore',
        ),
    ], [InlineKeyboardButton(text=day, callback_data='ignore') for day in ALL_WEEKDAYS]]

    for week in month_calendar:
        calendar_row = []
        for day in week:
            if day == 0:
                calendar_row.append(InlineKeyboardButton(text="-",
                                                         callback_data='ignore'))
                continue
            calendar_row.append(InlineKeyboardButton(
                text=str(day),
                callback_data=day
            ))
        keyboard.append(calendar_row)

    return InlineKeyboardMarkup(inline_keyboard=keyboard, row_width=7)
