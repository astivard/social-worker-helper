from src.tgbot.constants.weekdays import full_weekday_names


def get_privileges_case(is_person_privileged: str) -> str:
    return 'является' if is_person_privileged == 'да' else 'не является'


def format_number_of_visits_case(number_of_visits: int) -> str:
    return 'раза' if number_of_visits in (2, 3, 4, 22, 23, 24) else 'раз'


def format_weekdays_list(weekdays: list) -> str:
    full_weekdays = [full_weekday_names[weekday] for weekday in weekdays]
    sorted_weekdays = sorted(full_weekdays, key=lambda weekday: weekday[1])
    full_sorted_weekdays = [weekday[0] for weekday in sorted_weekdays]
    weekdays_string = '\n'.join(full_sorted_weekdays)
    weekdays_string = f'<b>{weekdays_string}</b>'
    return weekdays_string
