from src.tgbot.constants.weekdays import full_weekday_names

WITH_INFRASTRUCTURE_BTN = 'С инфраструктурой'
WITHOUT_INFRASTRUCTURE_BTN = 'Без инфраструктуры'

UNPRIVILEGED_PERSON_BTN = 'Полная оплата'
PRIVILEGED_PERSON_BTN = 'Частичная оплата (60%)'
MARRIED_COUPLES_50 = 'Семейные пары (50%)'
MARRIED_COUPLES_80 = 'Семейные пары (80%)'

PAYMENT_TYPES_BTN = (UNPRIVILEGED_PERSON_BTN, PRIVILEGED_PERSON_BTN,
                     MARRIED_COUPLES_50, MARRIED_COUPLES_80)

SET_VISITING_PERIODS_BTN = 'Задать/убрать периоды посещений'
START_NEW_CALCULATION_BTN = 'Начать новый расчет'

CHOOSE_All_WEEK_BTN = 'Выбрать всю неделю'
CALCULATE_BTN = 'Рассчитать'
CALCULATE_FOR_ALL_MONTH_BTN = 'Считать за весь месяц'
SET_ALL_PERIODS_BTN = 'Установить периоды'
DELETE_ALL_PERIODS_BTN = 'Удалить периоды'

WEEKDAYS = [weekday.upper() for weekday in full_weekday_names]

ALL_WEEKDAYS = WEEKDAYS + ['СБ', 'ВС']

FOR_REBOOT_BUTTONS = [SET_ALL_PERIODS_BTN, DELETE_ALL_PERIODS_BTN,
                      CHOOSE_All_WEEK_BTN, CALCULATE_BTN, *WEEKDAYS, *PAYMENT_TYPES_BTN]
