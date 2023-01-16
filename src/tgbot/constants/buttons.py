from src.tgbot.constants.weekdays import full_weekday_names

YES_BTN = 'ДА'
NO_BTN = 'НЕТ'

SET_VISITING_PERIODS_BTN = 'Задать/убрать периоды посещений'
START_NEW_CALCULATION_BTN = 'Начать новый расчет'

CHOOSE_All_WEEK_BTN = 'Выбрать всю неделю'
CALCULATE_BTN = 'Рассчитать'
CALCULATE_FOR_ALL_MONTH_BTN = 'Считать за весь месяц'
SET_ALL_PERIODS_BTN = 'Установить периоды'
DELETE_ALL_PERIODS_BTN = 'Удалить периоды'

WEEKDAYS = [weekday.upper() for weekday in full_weekday_names.keys()]

ALL_WEEKDAYS = WEEKDAYS + ['СБ', 'ВС']

FOR_REBOOT_BUTTONS = [SET_ALL_PERIODS_BTN, DELETE_ALL_PERIODS_BTN,
                      CHOOSE_All_WEEK_BTN, CALCULATE_BTN, *WEEKDAYS]
