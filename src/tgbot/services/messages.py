from src.tgbot.services.utils import (get_current_month_name,
                                      get_number_of_visits_case)


def get_total_message(data: tuple) -> str:
    total, number_of_visit_days, day_care_cost, month, from_date = data
    result_message = f"Вы посетили клиента начиная c <b>{from_date}</b> <i>{month}</i> " \
                     f"<b>{number_of_visit_days}</b> " \
                     f"{get_number_of_visits_case(number_of_visit_days)}.\n\n" \
                     f"Сумма:     <code>{number_of_visit_days} * {day_care_cost} = {total}</code>     руб."
    return result_message


def get_from_date_message(msg: str) -> str:
    result_message = f'⚠️Ваши дальнейшие расчеты будут начинаться с ' \
                     f'<b><i>{msg} {get_current_month_name(case="2")}</i></b>.'
    return result_message


def get_privileges_message() -> str:
    result_message = "Выберите, является ли клиент льготником: 👇🏻"
    return result_message


def get_help_msg() -> str:
    result_message = '<b>Доступные команды бота:</b>\n\n' \
                     '/start - перезапуск бота\n' \
                     '/calc - начать новый расчет\n' \
                     '/date - задать/убрать дату расчета\n' \
                     '/help - помощь\n\n' \
                     'Для быстрого вызова команд используйте кнопку меню.\n\n' \
                     'Для начала расчета используйте команду /calc или кнопку <b>Начать новый расчет</b>.\n\n' \
                     'Если вы хотите считать стоимость обслуживания с определенного числа месяца, ' \
                     'используйте команду /date или кнопку <b>Задать/убрать дату отсчета</b>. 👇'
    return result_message


def get_welcome_msg() -> str:
    result_message = 'Добро пожаловать в Помощник для соцработника 👋\n\n' \
                     f'{get_help_msg()}'
    return result_message


def get_reboot_msg() -> str:
    result_message = '⚠️Бот был перезагружен в результате технических работ. ' \
                     f'Дата отсчета установлена на <b>1 {get_current_month_name("2")}</b> текущего месяца.\n\n' \
                     'Пожалуйста, установите (при надобности) нужную Вам дату отсчёта - /date ' \
                     'и начните новый расчет - /calc 👇🏻'
    return result_message
