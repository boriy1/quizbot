from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    lang = State()
    phone_number = State()
