from aiogram.dispatcher.filters.state import State, StatesGroup

class AddLocation(StatesGroup):
    location = State()
    

class AddLocationRu(StatesGroup):
    location = State()