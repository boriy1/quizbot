from aiogram.dispatcher.filters.state import State, StatesGroup


class SendComment(StatesGroup):
    text = State()
    

class SendCommentRu(StatesGroup):
    text = State()