from src.tgbot.services.tools import get_days_in_current_month

# (with infrastructure, without infrastructure)
tariffs = {
    "unprivileged_person": (1.37, 2.00),
    "privileged_person": (0.82, 1.20),
    "married_couples_50": (0.69, 1.00),
    "married_couples_80": (1.10, 1.60),
}

available_privileges = ('да', 'нет')
available_weekdays = ('пн', 'вт', 'ср', 'чт', 'пт')
available_month_days_numbers = [str(day) for day in range(1, get_days_in_current_month() + 1)]

full_weekday_names = {
    'пн': ('Понедельник', 1),
    'вт': ('Вторник', 2),
    'ср': ('Среда', 3),
    'чт': ('Четверг', 4),
    'пт': ('Пятница', 5)
}

correct_month_names = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}

holidays_2023 = ((2,),  # January
                 (0,),  # February
                 (8,),  # March
                 (25,),  # April
                 (1, 9),  # May
                 (0,),  # June
                 (3,),  # July
                 (0,),  # August
                 (0,),  # September
                 (0,),  # October
                 (7,),  # November
                 (25,))  # December
