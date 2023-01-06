from calendar import monthcalendar
from datetime import datetime

from src.tgbot.constants.holidays import holidays_2023
from src.tgbot.constants.tariffs import tariffs
from src.tgbot.constants.weekdays import full_weekday_names
from src.tgbot.tools.month import get_current_month_name


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


