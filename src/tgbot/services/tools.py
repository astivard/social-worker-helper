from calendar import monthrange
from datetime import datetime


def get_days_in_current_month() -> int:
    month = datetime.now().month
    year = datetime.now().year
    return monthrange(year, month)[1]
