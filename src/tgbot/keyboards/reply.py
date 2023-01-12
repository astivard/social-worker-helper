from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

from src.tgbot.constants.buttons import *


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=YES_BTN),
         types.KeyboardButton(text=NO_BTN)],
        [types.KeyboardButton(text=SET_VISITING_PERIOD_BTN)]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb,
                                     resize_keyboard=True)


def get_weekdays_kb() -> ReplyKeyboardMarkup:
    buttons = [
        [types.KeyboardButton(text=weekday) for weekday in WEEKDAYS],
        [types.KeyboardButton(text=CHOOSE_All_WEEK_BTN)],
        [types.KeyboardButton(text=CALCULATE_BTN)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons,
                                     resize_keyboard=True)


def get_new_calc_kb() -> ReplyKeyboardMarkup:
    buttons = [
        [types.KeyboardButton(text=START_NEW_CALCULATION_BTN)],
        [types.KeyboardButton(text=SET_VISITING_PERIOD_BTN)]
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons,
                                     resize_keyboard=True)


def get_cancel_from_date_kb() -> ReplyKeyboardMarkup:
    buttons = [
        [types.KeyboardButton(text=CALCULATE_FOR_ALL_MONTH_BTN)]
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons,
                                     resize_keyboard=True)
