from aiogram.fsm.state import State, StatesGroup


class CaringCost(StatesGroup):
    privileges = State()
    weekdays = State()
    period = State()
