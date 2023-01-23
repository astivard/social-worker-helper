from src.tgbot.constants.buttons import (SET_VISITING_PERIODS_BTN,
                                         START_NEW_CALCULATION_BTN)
from src.tgbot.constants.holidays import holidays_2023
from src.tgbot.constants.months import correct_month_names
from src.tgbot.constants.tariffs import tariffs
from src.tgbot.tools.formatters import format_number_of_visits_case
from src.tgbot.tools.month import get_current_month_name
from src.tgbot.tools.scripts import check_infrastructure


def get_total_message(data: tuple) -> str:
    total, visiting_days_data, number_of_days_data, tariff, month, periods, infrastructure, payment_type = data

    if type(periods[0]) != list:
        start_day = periods[0]
        end_day = periods[1]
        res_msg = '\n'.join(
            [f"<b>{weekday}</b>:   <i>{day}</i> {month}" for weekday, day in number_of_days_data])
    else:
        full_period_days = [day for period in periods for day in period]
        start_day = min(full_period_days)
        end_day = max(full_period_days)
        periods_msg = []
        for period in periods:
            if period:
                minor_period = f"\n<b>C {period[0]} по {period[1]} {get_current_month_name()}:</b>\n"
                weekdays_info_msg = '\n'.join(
                    [f"<b>{weekday}</b>:   <i>{day}</i> {month}" for weekday, day in number_of_days_data
                     if period[0] <= day <= period[1]])
                weekdays_info_msg = weekdays_info_msg if weekdays_info_msg else 'Нет посещений'
                weekdays_info_msg = f"{minor_period}{weekdays_info_msg}"
                periods_msg.append(weekdays_info_msg)
        res_msg = "\n".join(periods_msg)

    result_message = f"Вы посетили клиента с <b>{start_day} по {end_day}</b> <i>{month}</i> " \
                     f"<b>{visiting_days_data}</b> " \
                     f"{format_number_of_visits_case(visiting_days_data)}.\n\n" \
                     f"<b>Ваши посещения:</b>\n\n{res_msg}.\n\n" \
                     f"<b>Клиент:\n</b>{infrastructure}\n{payment_type}\n" \
                     f"тариф — {tariff} руб.\n\n" \
                     f"Итог:     <code>{visiting_days_data} * {tariff} = {total}</code>     руб."
    return result_message


def get_new_user_msg(fullname: str, username: str, user_id: int) -> str:
    result_message = '#new_user\n' \
                     f'Имя: {fullname}\n' \
                     f'username: @{username}\n' \
                     f'id: <a href="tg://user?id={user_id}">{user_id}</a>'
    return result_message


def get_incorrect_msg_from_user(username: str, user_id: int, msg: str) -> str:
    result_message = '#msg_from_user\n' \
                     f'username: @{username}\n' \
                     f'id: <a href="tg://user?id={user_id}">{user_id}</a>\n\n' \
                     f'<i>{msg}</i>'
    return result_message


def get_current_month_holidays_msg():
    non_working_holidays = {}
    for month_number, month in enumerate(holidays_2023):
        if 0 not in month:
            non_working_holidays[correct_month_names[month_number + 1]] = month

    result_msg = '\n'.join([f'<i>{", ".join(list(map(str, holidays)))}</i>   {month}' for month, holidays in
                            non_working_holidays.items()])
    transfers = "<b>Переносы рабочих дней:</b>\n\n" \
                "с понедельника 24 апреля на субботу 29 апреля\n" \
                "с понедельника 8 мая на субботу 13 мая\n" \
                "c понедельника 6 ноября на субботу 11 ноября\n"
    return f'<b>Нерабочие праздничные дни:</b>\n\n{result_msg}\n\n{transfers}'


def get_period_alert_msg(is_start_period: bool, callback_data: str) -> str:
    if is_start_period:
        msg = f"Вы выбрали начало периода — {callback_data} {get_current_month_name()}.\n\n" \
              f"Теперь выберите конец периода.\n\n" \
              f"Подсказка: если Вам нужно задать период в один день, " \
              f"выберите конец периода как тот же день."
    else:
        msg = f"Вы выбрали конец периода — {callback_data} {get_current_month_name()}.\n\n" \
              f"Для выбора следующего периода снова выберите начало и конец периода.\n\n" \
              f"Подсказка: после установки нужных периодов нажмите Установить периоды."
    return msg


def get_periods_msg(periods: list[list]) -> str:
    msg = []
    for period in periods:
        if len(period) == 1:
            period.append(period[0])
        if period:
            if period[0] == period[1]:
                msg.append(f"{period[0]} <i>{get_current_month_name()}</i>")
            else:
                msg.append(f'{period[0]} — {period[1]} <i>{get_current_month_name()}</i>')
    return '\n'.join(msg)


def get_calendar_period_msg(periods: list) -> str:
    msg = "⬆️ Установите периоды ⬆️"
    if periods:
        return f"{msg}\nУ вас установлены <b>периоды посещений</b>:\n" \
               f"<b>{get_periods_msg(periods=periods)}</b> "
    return msg


def get_setting_period_msg(periods: list) -> str:
    if periods:
        return f"Вы установили <b>периоды посещений</b>:\n" \
               f"<b>{get_periods_msg(periods=periods)}</b> " \
               f"\n\n{after_setting_or_deleting_periods_msg}"
    return f"⚠️ Вы не выбрали ни одного периода.\n\n{after_setting_or_deleting_periods_msg}"


def get_deleting_periods_msg(periods: list) -> str:
    if periods:
        return f'⚠️ Периоды успешно удалены.\n\n{after_setting_or_deleting_periods_msg}'
    return f'⚠️ В данный момент у Вас не установлен ни один период расчета.\n\n{after_setting_or_deleting_periods_msg}'


chose_weekdays_msg = "Выберите дни недели (либо всю неделю целиком), " \
                     "в которые обслуживается клиент, затем нажмите рассчитать: 👇🏻"

empty_weekdays_list_msg = f"❗️Вы не выбрали ни одного дня недели!\n\n{chose_weekdays_msg}"

incorrect_period_msg = "Нельзя выбрать этот день!"

infrastructure_msg = "Выберите наличие инфраструктуры у клиента: 👇🏻"

unavailable_periods_kb_msg = "Данная клавиатура устарела! Воспользуйтесь новой, нажав\n" \
                             f"{SET_VISITING_PERIODS_BTN}"

after_setting_or_deleting_periods_msg = "Начните новый расчет с помощью кнопки\n" \
                                        f"<b>{START_NEW_CALCULATION_BTN}</b>.\n\nДля задания или удаления периодов " \
                                        "расчета нажмите\n" \
                                        f"<b>{SET_VISITING_PERIODS_BTN}</b> 👇🏻"


def get_pay_type_msg(with_infrastructure: str) -> str:
    with_infrastructure = check_infrastructure(with_infrastructure=with_infrastructure)
    if with_infrastructure:
        return f"{tariffs_msg[22:290]}Выберите тип оплаты: 👇🏻"
    return f"{tariffs_msg[290:]}Выберите тип оплаты: 👇🏻"


help_msg = '<b>Доступные команды бота:</b>\n\n' \
           '/start — перезапуск бота (используйте при возникновении каких-либо неполадок)\n' \
           f'/calc — {START_NEW_CALCULATION_BTN.lower()}\n' \
           '/date — задать периоды посещений\n' \
           '/help — помощь\n' \
           '/tariffs — текущие тарифы\n' \
           '/holidays — нерабочие праздничные дни\n\n' \
           'Для быстрого вызова команд используйте кнопку меню.\n\n' \
           f'Для начала расчета используйте команду /calc или кнопку <b>{START_NEW_CALCULATION_BTN}</b>.\n\n' \
           'Если вы хотите считать стоимость обслуживания в определенные периоды месяца, ' \
           f'используйте команду /date или кнопку <b>{SET_VISITING_PERIODS_BTN}</b>. 👇'

welcome_msg = 'Добро пожаловать в Помощник для соцработника 👋\n\n' \
              f'{help_msg}'

reboot_msg = '⚠️Бот был перезагружен в результате технических работ. ' \
             'Введенные Вами ранее данные были удалены. ' \
             'Расчет будет производится <b>за весь текущий месяц</b>.\n\n' \
             'Пожалуйста, установите (при надобности) периоды посещений - /date ' \
             'и начните новый расчет - /calc 👇🏻'

tariffs_msg = '<b>Текущие тарифы:</b>\n\n' \
              f'<i>1) c наличием инфрастуктуры (1 час 50 минут):</i>\n\n' \
              f'☑️полная оплата (100%):\n     ' \
              f'<code>{tariffs["unprivileged_person"][0]} </code> руб.\n\n' \
              f'☑️частичная оплата (60%):\n     ' \
              f'<code>{tariffs["privileged_person"][0]} </code>руб.\n\n' \
              f'☑️семейные пары (50%):\n     ' \
              f'<code>{tariffs["married_couples_50"][0]} </code>руб.\n\n' \
              f'☑️семейные пары (80%):\n     ' \
              f'<code>{tariffs["married_couples_80"][0]} </code>руб.\n\n' \
              f'<i>2) без наличия инфрастуктуры (2 часа 40 минут):</i>\n\n' \
              f'☑️полная оплата (100%):\n     ' \
              f'<code>{tariffs["unprivileged_person"][1]} </code> руб.\n\n' \
              f'☑️частичная оплата (60%):\n     ' \
              f'<code>{tariffs["privileged_person"][1]} </code>руб.\n\n' \
              f'☑️семейные пары (50%): \n     ' \
              f'<code>{tariffs["married_couples_50"][1]} </code>руб.\n\n' \
              f'☑️семейные пары (80%): \n     ' \
              f'<code>{tariffs["married_couples_80"][1]} </code>руб.\n\n'
