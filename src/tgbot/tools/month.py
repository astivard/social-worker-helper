from calendar import monthrange
from datetime import datetime

from src.tgbot.constants.months import correct_month_names


def get_days_in_current_month() -> int:
    month = datetime.now().month
    year = datetime.now().year
    return monthrange(year, month)[1]


def _get_current_month_number() -> int:
    return datetime.now().month


def get_current_month_name() -> str:
    return correct_month_names[_get_current_month_number()]


def get_available_month_days_numbers() -> list:
    return [str(day) for day in range(1, get_days_in_current_month() + 1)]
