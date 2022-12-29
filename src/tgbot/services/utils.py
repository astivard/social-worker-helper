from calendar import monthcalendar
from datetime import datetime

from src.tgbot.services.data import (correct_month_names_1,
                                     correct_month_names_2, full_weekday_names,
                                     holidays_2022, holidays_2023,
                                     tariffs_with_infrastructure)


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
    holidays = holidays_2022 if year == 2022 else holidays_2023
    month_holidays = holidays[month - 1]
    from_date = int(data.get('from_date', 1))

    for day in data['weekdays']:
        weekday = full_weekday_names[day][1] - 1
        number_of_visit_days += len([1 for i in month_weeks if i[weekday] != 0
                                     and i[weekday] >= from_date
                                     and i[weekday] not in month_holidays])

    return number_of_visit_days


def get_total(user_data: dict) -> tuple:
    month = get_current_month_name(case='2')
    number_of_days = get_number_days(user_data)
    is_privileged = True if user_data['privilege'] == 'да' else False
    day_care_cost = tariffs_with_infrastructure["privileged_person"] if \
        is_privileged else tariffs_with_infrastructure["unprivileged_person"]
    from_date = int(user_data.get('from_date', 1))
    total = round(number_of_days * day_care_cost, 2)
    result = (total, number_of_days, day_care_cost, month, from_date)
    return result


def get_number_of_visits_case(number_of_visits: int) -> str:
    """Возвращает слово 'раз' или 'раза' в зависимости от числа посещений"""

    return 'раза' if number_of_visits in (2, 3, 4, 22, 23, 24) else 'раз'


def get_current_month_name(case: str) -> str:
    correct_month_names = correct_month_names_1 if case == '1' else correct_month_names_2
    return correct_month_names[datetime.now().month]
