from aiogram.fsm.state import State, StatesGroup


class CaringCost(StatesGroup):
    infrastructure = State()
    privileges = State()
    weekdays = State()
    period = State()
