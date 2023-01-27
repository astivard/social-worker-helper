from calendar import monthrange
from datetime import datetime

from src.tgbot.constants.months import correct_month_names


def get_days_in_current_month() -> int:
    month, year = get_current_month_and_year_number()
    return monthrange(year, month)[1]


def get_current_month_and_year_number() -> tuple[int, int]:
    month = datetime.now().month
    year = datetime.now().year
    return month, year


def _get_current_month_number() -> int:
    return datetime.now().month


def get_current_month_name(is_prepositional: bool = False,
                           is_nominative: bool = False) -> str:
    current_month_number = _get_current_month_number()
    if is_prepositional:
        return f"{correct_month_names[current_month_number][:-1]}е"
    elif is_nominative:
        current_month_number = _get_current_month_number()
        if current_month_number == 3:
            return 'март'
        elif current_month_number == 5:
            return 'апрель'
        elif current_month_number == 8:
            return 'август'
        else:
            return f"{correct_month_names[current_month_number][:-1]}ь"
    return correct_month_names[current_month_number]


def get_available_month_days_numbers() -> list:
    return [str(day) for day in range(1, get_days_in_current_month() + 1)]
