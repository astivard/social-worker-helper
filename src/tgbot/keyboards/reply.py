from aiogram import types
from aiogram.types import ReplyKeyboardMarkup


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text='ДА'),
         types.KeyboardButton(text='НЕТ')],
        [types.KeyboardButton(text='Задать/убрать дату отсчета')]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb,
                                     resize_keyboard=True)


def get_weekdays_kb() -> ReplyKeyboardMarkup:
    weekdays = ('ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ')
    buttons = [
        [types.KeyboardButton(text=weekday) for weekday in weekdays],
        [types.KeyboardButton(text='Рассчитать')],
        [types.KeyboardButton(text='Начать новый расчет')]
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons,
                                     resize_keyboard=True)


def get_new_calc_kb() -> ReplyKeyboardMarkup:
    buttons = [
        [types.KeyboardButton(text='Начать новый расчет')],
        [types.KeyboardButton(text='Задать/убрать дату отсчета')]
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons,
                                     resize_keyboard=True)


def get_cancel_from_date_kb() -> ReplyKeyboardMarkup:
    buttons = [
        [types.KeyboardButton(text='Считать за весь месяц')]
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons,
                                     resize_keyboard=True)
