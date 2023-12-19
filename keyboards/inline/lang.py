from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("O'zbekcha🇺🇿", callback_data='uz'),
        InlineKeyboardButton("Русский🇷🇺", callback_data='ru')
    ]
])