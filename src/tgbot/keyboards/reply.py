from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

from src.tgbot.constants.buttons import *


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    keyboard = [
        [types.KeyboardButton(text=YES_BTN),
         types.KeyboardButton(text=NO_BTN)],
        [types.KeyboardButton(text=SET_VISITING_PERIODS_BTN)]
    ]
    return types.ReplyKeyboardMarkup(keyboard=keyboard,
                                     resize_keyboard=True)


def get_weekdays_kb() -> ReplyKeyboardMarkup:
    keyboard = [
        [types.KeyboardButton(text=weekday) for weekday in WEEKDAYS],
        [types.KeyboardButton(text=CHOOSE_All_WEEK_BTN)],
        [types.KeyboardButton(text=CALCULATE_BTN)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=keyboard,
                                     resize_keyboard=True)


def get_new_calc_kb(is_short_kb: bool = False) -> ReplyKeyboardMarkup:
    keyboard = [
        [types.KeyboardButton(text=START_NEW_CALCULATION_BTN)],
        [types.KeyboardButton(text=SET_VISITING_PERIODS_BTN)]
    ]
    if is_short_kb:
        keyboard.pop(1)
    return types.ReplyKeyboardMarkup(keyboard=keyboard,
                                     resize_keyboard=True)


def get_cancel_period_kb() -> ReplyKeyboardMarkup:
    keyboard = [
        [types.KeyboardButton(text=SET_ALL_PERIODS_BTN),
         types.KeyboardButton(text=DELETE_ALL_PERIODS_BTN)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=keyboard,
                                     resize_keyboard=True)
