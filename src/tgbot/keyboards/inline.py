import calendar
import locale

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.tgbot.constants.buttons import ALL_WEEKDAYS
from src.tgbot.tools.month import get_current_month_and_year_number

locale.setlocale(locale.LC_ALL, 'ru_RU')

month, year = get_current_month_and_year_number()


def get_calendar_kb() -> InlineKeyboardMarkup:
    month_calendar = calendar.monthcalendar(year, month)
    keyboard = [[
        InlineKeyboardButton(
            text=f'{calendar.month_name[month]} {str(year)}',
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
