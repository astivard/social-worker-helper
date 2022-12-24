from aiogram.fsm.state import State, StatesGroup


class CaringCost(StatesGroup):
    privileges = State()
    weekdays = State()
    from_date = State()