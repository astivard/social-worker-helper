from calendar import monthcalendar
from datetime import datetime

from src.tgbot.constants.holidays import holidays_2023
from src.tgbot.constants.tariffs import tariffs
from src.tgbot.constants.weekdays import full_weekday_names
from src.tgbot.tools.month import (get_current_month_name,
                                   get_days_in_current_month)


def _get_first_last_days_of_period(period: list[int]) -> tuple[int, int]:
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
                start_day, end_day = _get_first_last_days_of_period(period=period)
                weekday = full_weekday_names[day][1] - 1
                for i in month_weeks:
                    if i[weekday] != 0 \
                            and start_day <= i[weekday] <= end_day \
                            and i[weekday] not in month_holidays:
                        res.append((day, i[weekday]))
    return sorted(res, key=lambda t: t[1])


def check_infrastructure(with_infrastructure: str) -> bool:
    return True if with_infrastructure == 'с инфраструктурой' else False


def get_tariffs_key(payment_type: str) -> str:
    if payment_type == 'полная оплата':
        return 'unprivileged_person'
    elif payment_type == 'частичная оплата (60%)':
        return 'privileged_person'
    elif payment_type == 'семейные пары (50%)':
        return 'married_couples_50'
    else:
        return 'married_couples_80'


def _get_tariff(user_data: dict) -> int:
    with_infrastructure = check_infrastructure(user_data['with_infrastructure'])
    tariffs_key = get_tariffs_key(user_data['privilege'])
    if with_infrastructure:
        return tariffs[tariffs_key][0]
    return tariffs[tariffs_key][1]


def get_total(user_data: dict) -> tuple:
    month = get_current_month_name()
    visiting_days_data = get_visiting_days(user_data)
    number_of_days = len(visiting_days_data)

    tariff = _get_tariff(user_data=user_data)
    periods = user_data.get('periods', [1, get_days_in_current_month()])

    if not periods:
        periods = [1, get_days_in_current_month()]

    infrastructure = user_data['with_infrastructure']
    payment_type = user_data['privilege']

    total = round(number_of_days * tariff, 2)
    result = (total, number_of_days, visiting_days_data, tariff, month, periods, infrastructure, payment_type)
    return result


def is_new_value_correct(periods: list[list], new_value: int) -> bool:
    period_days = [day for period in periods for day in period]
    if period_days:
        if new_value < max(period_days):
            return False
    return True
