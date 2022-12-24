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
