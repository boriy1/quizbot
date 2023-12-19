from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


settings = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Tilni o'zgartirish", callback_data='set_lang')
    ],
    [
        InlineKeyboardButton("⬅️ Ortga", callback_data='back')
    ]
])


settings_ru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Изменить язык", callback_data='set_lang')
    ],
    [
        InlineKeyboardButton("⬅️ Назад", callback_data='back_ru')
    ]
])