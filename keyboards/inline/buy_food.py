from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buy_food = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🛒 Savatga qo'shish", callback_data='add_cart')
    ],
    [
        InlineKeyboardButton("⬅️ Ortga", callback_data='back')
    ]
])


buy_food_ru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🛒 Добавить в корзину", callback_data='add_cart_ru')
    ],
    [
        InlineKeyboardButton("⬅️ Назад", callback_data='back_ru')
    ]
])