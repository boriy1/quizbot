from aiogram.dispatcher.filters.state import State, StatesGroup

class Confirm(StatesGroup):
    check = State()
    location = State()
    
    
class ConfirmRu(StatesGroup):
    check = State()
    location = State()