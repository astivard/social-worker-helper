from calendar import monthcalendar
from datetime import datetime

from src.tgbot.constants.holidays import holidays_2023
from src.tgbot.constants.tariffs import tariffs
from src.tgbot.constants.weekdays import full_weekday_names
from src.tgbot.tools.month import (get_current_month_name,
                                   get_days_in_current_month)


def _get_start_end_days_of_period(period: list[int]) -> tuple[int, int]:
    period_len = len(period)
    if period_len == 1:
        return period[0], period[0]
    return period[0], period[1]


def get_visiting_days(data: dict) -> list[tuple]:
    month = datetime.now().month
    year = datetime.now().year
    month_weeks = monthcalendar(year, month)
    month_holidays = holidays_2023[month - 1]
    periods = data.get('periods')  # [[],[]]

    if not periods:
        periods = [[1, get_days_in_current_month()]]

    res = []
    for day in data['weekdays']:
        for period in periods:
            if period:
                start_day, end_day = _get_start_end_days_of_period(period=period)
                weekday = full_weekday_names[day][1] - 1
                for i in month_weeks:
                    if i[weekday] != 0 \
                            and start_day <= i[weekday] <= end_day \
                            and i[weekday] not in month_holidays:
                        res.append((day, i[weekday]))
    return sorted(res, key=lambda t: t[1])


def get_total(user_data: dict) -> tuple:
    month = get_current_month_name()
    visiting_days_data = get_visiting_days(user_data)
    number_of_days = len(visiting_days_data)
    is_privileged = True if user_data['privilege'] == 'да' else False
    day_care_cost = tariffs["privileged_person"][0] if \
        is_privileged else tariffs["unprivileged_person"][0]
    periods = user_data.get('periods', [1, get_days_in_current_month()])

    if not periods:
        periods = [1, get_days_in_current_month()]

    total = round(number_of_days * day_care_cost, 2)
    result = (total, number_of_days, visiting_days_data, day_care_cost, month, periods)
    return result


def is_new_value_correct(periods: list[list], new_value: int) -> bool:
    period_days = [day for period in periods for day in period]
    if period_days:
        if new_value < max(period_days):
            return False
    return True
