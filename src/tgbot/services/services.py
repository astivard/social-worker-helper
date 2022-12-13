from calendar import monthcalendar
from datetime import datetime

from tgbot.services.data import (correct_month_names, full_weekday_names,
                                 holidays_2022, holidays_2023,
                                 privileged_person_day_care_cost,
                                 unprivileged_person_day_care_cost)


def check_privileges(is_person_privileged: str) -> str:
    return 'является' if is_person_privileged == 'да' else 'не является'


def format_weekdays_list(weekdays: list) -> str:
    full_weekdays = [full_weekday_names[weekday] for weekday in weekdays]
    sorted_weekdays = sorted(full_weekdays, key=lambda weekday: weekday[1])
    full_sorted_weekdays = [weekday[0] for weekday in sorted_weekdays]
    weekdays_string = '\n'.join(full_sorted_weekdays)
    weekdays_string = f'<b>{weekdays_string}</b>'
    return weekdays_string


def get_number_days(week_days: list) -> int:
    number_of_visit_days = 0
    month = datetime.now().month
    year = datetime.now().year
    holidays = holidays_2022 if year == 2022 else holidays_2023

    for day in week_days:
        number_of_visit_days += len([1 for i in monthcalendar(year, month) if
                                     i[full_weekday_names[day][1]] != 0 and i[full_weekday_names[day][1]] not in
                                     holidays[month - 1]])
    return number_of_visit_days


def get_total(user_data: dict) -> str:
    month = correct_month_names[datetime.now().month]
    number_of_days = get_number_days(user_data['weekdays'])
    is_privileged = True if user_data['privilege'] == 'да' else False
    day_care_cost = privileged_person_day_care_cost if is_privileged else unprivileged_person_day_care_cost
    total = round(number_of_days * day_care_cost, 2)
    result = _format_total_output(data=(total, number_of_days, day_care_cost, month))
    return result


def _format_total_output(data: tuple) -> str:
    total, number_of_visit_days, day_care_cost, month = data
    result_message = f"Вы посетили пожилого в <i>{month}</i> <b>{number_of_visit_days}</b> раз(а).\n\n" \
                     f"Сумма:     <code>{number_of_visit_days} * {day_care_cost} = {total}</code>     руб."
    return result_message
