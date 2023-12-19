from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


check = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("✅ Buyurtma berish", callback_data='confirmed'),
        InlineKeyboardButton("🛒 Savatni tozalash", callback_data='clear')
    ],
    [
        InlineKeyboardButton("⬅️ Ortga", callback_data='back')
    ]
])


check_ru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("✅ Разместить заказ", callback_data='confirmed'),
        InlineKeyboardButton("🛒 Очистить корзину", callback_data='clear')
    ],
    [
        InlineKeyboardButton("⬅️ Ortga", callback_data='back_ru')
    ]
])