from src.tgbot.services.tools import get_days_in_current_month

tariffs_with_infrastructure = {
    "unprivileged_person": 1.37,
    "privileged_person": 0.82,
    "married_couples_50": 0.69,
    "married_couples_80": 1.10,
}

tariffs_without_infrastructure = {
    "unprivileged_person": 2.00,
    "privileged_person": 1.20,
    "married_couples_50": 1.00,
    "married_couples_80": 1.60,
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

correct_month_names_1 = {
    1: "январе",
    2: "феврале",
    3: "марте",
    4: "апреле",
    5: "мае",
    6: "июне",
    7: "июле",
    8: "августе",
    9: "сентябре",
    10: "октябре",
    11: "ноябре",
    12: "декабре"
}

correct_month_names_2 = {
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

holidays_2022 = ((7,),  # Январь
                 (0,),  # Февраль
                 (8,),  # Март
                 (0,),  # Апрель
                 (3, 9),  # Май
                 (0,),  # Июнь
                 (0,),  # Июль
                 (0,),  # Август
                 (0,),  # Сентрябрь
                 (0,),  # Октябрь
                 (7,),  # Ноябрь
                 (0,))  # Декабрь

holidays_2023 = ((2,),  # Январь
                 (0,),  # Февраль
                 (8,),  # Март
                 (25,),  # Апрель
                 (1, 9),  # Май
                 (0,),  # Июнь
                 (3,),  # Июль
                 (0,),  # Август
                 (0,),  # Сентябрь
                 (0,),  # Октябрь
                 (7,),  # Ноябрь
                 (25,))  # Декабрь
