from calendar import monthcalendar
from datetime import datetime

from src.tgbot.services.data import (correct_month_names, full_weekday_names,
                                     holidays_2023, tariffs)


def check_privileges(is_person_privileged: str) -> str:
    return 'является' if is_person_privileged == 'да' else 'не является'


def format_weekdays_list(weekdays: list) -> str:
    full_weekdays = [full_weekday_names[weekday] for weekday in weekdays]
    sorted_weekdays = sorted(full_weekdays, key=lambda weekday: weekday[1])
    full_sorted_weekdays = [weekday[0] for weekday in sorted_weekdays]
    weekdays_string = '\n'.join(full_sorted_weekdays)
    weekdays_string = f'<b>{weekdays_string}</b>'
    return weekdays_string


def get_number_days(data: dict) -> int:
    number_of_visit_days = 0
    month = datetime.now().month
    year = datetime.now().year
    month_weeks = monthcalendar(year, month)
    month_holidays = holidays_2023[month - 1]
    from_date = int(data.get('from_date', 1))

    for day in data['weekdays']:
        weekday = full_weekday_names[day][1] - 1
        number_of_visit_days += len([1 for i in month_weeks if i[weekday] != 0
                                     and i[weekday] >= from_date
                                     and i[weekday] not in month_holidays])

    return number_of_visit_days


def get_total(user_data: dict) -> tuple:
    month = get_current_month_name()
    number_of_days = get_number_days(user_data)
    is_privileged = True if user_data['privilege'] == 'да' else False
    day_care_cost = tariffs["privileged_person"][0] if \
        is_privileged else tariffs["unprivileged_person"][0]
    from_date = int(user_data.get('from_date', 1))
    total = round(number_of_days * day_care_cost, 2)
    result = (total, number_of_days, day_care_cost, month, from_date)
    return result


def get_number_of_visits_case(number_of_visits: int) -> str:
    return 'раза' if number_of_visits in (2, 3, 4, 22, 23, 24) else 'раз'


def get_current_month_number() -> int:
    return datetime.now().month


def get_current_month_name() -> str:
    return correct_month_names[get_current_month_number()]
