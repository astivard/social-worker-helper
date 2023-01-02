from src.tgbot.services.data import tariffs
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
                     f'<b><i>{msg} {get_current_month_name()}</i></b>.'
    return result_message


privileges_message = "Выберите, является ли клиент льготником: 👇🏻"

help_msg = '<b>Доступные команды бота:</b>\n\n' \
           '/start - перезапуск бота\n' \
           '/calc - начать новый расчет\n' \
           '/date - задать/убрать дату расчета\n' \
           '/help - помощь\n\n' \
           'Для быстрого вызова команд используйте кнопку меню.\n\n' \
           'Для начала расчета используйте команду /calc или кнопку <b>Начать новый расчет</b>.\n\n' \
           'Если вы хотите считать стоимость обслуживания с определенного числа месяца, ' \
           'используйте команду /date или кнопку <b>Задать/убрать дату отсчета</b>. 👇'

welcome_msg = 'Добро пожаловать в Помощник для соцработника 👋\n\n' \
              f'{help_msg}'

reboot_msg = '⚠️Бот был перезагружен в результате технических работ. ' \
             f'Дата отсчета установлена на <b>1 {get_current_month_name()}</b> текущего месяца.\n\n' \
             'Пожалуйста, установите (при надобности) нужную Вам дату отсчёта - /date ' \
             'и начните новый расчет - /calc 👇🏻'

tariffs_msg = '<b>Текущие тарифы:</b>\n\n' \
              f'<i>1) c наличием инфрастуктуры (1 час 50 минут):</i>\n\n' \
              f'✔️полная оплата (100%):\n     ' \
              f'<code>{tariffs["unprivileged_person"][0]} </code> руб.\n\n' \
              f'✔️частичная оплата (60%):\n     ' \
              f'<code>{tariffs["privileged_person"][0]} </code>руб.\n\n' \
              f'✔️семейные пары (50%):\n     ' \
              f'<code>{tariffs["married_couples_50"][0]} </code>руб.\n\n' \
              f'✔️семейные пары (80%):\n     ' \
              f'<code>{tariffs["married_couples_80"][0]} </code>руб.\n\n' \
              f'<i>2) без наличия инфрастуктуры (2 часа 40 минут):</i>\n\n' \
              f'✔️полная оплата (100%):\n     ' \
              f'<code>{tariffs["unprivileged_person"][1]} </code> руб.\n\n' \
              f'✔️частичная оплата (60%):\n     ' \
              f'<code>{tariffs["privileged_person"][1]} </code>руб.\n\n' \
              f'✔️семейные пары (50%): \n     ' \
              f'<code>{tariffs["married_couples_50"][1]} </code>руб.\n\n' \
              f'✔️семейные пары (80%): \n     ' \
              f'<code>{tariffs["married_couples_80"][1]} </code>руб.\n\n'
