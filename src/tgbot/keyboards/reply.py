from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

from src.tgbot.constants.buttons import *


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


def get_infrastructure_kb() -> ReplyKeyboardMarkup:
    keyboard = [
        [types.KeyboardButton(text=WITH_INFRASTRUCTURE_BTN),
         types.KeyboardButton(text=WITHOUT_INFRASTRUCTURE_BTN)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=keyboard,
                                     resize_keyboard=True)


def get_client_type_kb() -> ReplyKeyboardMarkup:
    keyboard = [
        [types.KeyboardButton(text=UNPRIVILEGED_PERSON_BTN),
         types.KeyboardButton(text=PRIVILEGED_PERSON_BTN)],
        [types.KeyboardButton(text=MARRIED_COUPLES_50),
         types.KeyboardButton(text=MARRIED_COUPLES_80)]
    ]
    return types.ReplyKeyboardMarkup(keyboard=keyboard,
                                     resize_keyboard=True)
