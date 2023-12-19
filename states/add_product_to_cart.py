from aiogram.dispatcher.filters.state import State, StatesGroup


class AddProductToCart(StatesGroup):
    check = State()
    

class AddProductToCartRu(StatesGroup):
    check = State()