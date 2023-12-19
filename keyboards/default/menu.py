from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database import database as db
from functions.transliterate import to_cyrillic, to_latin



menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("🛒 Buyurtma qilish"),
        KeyboardButton("🛍 Buyurtmalarim")
    ],
    [
        KeyboardButton("📍 Joylashuvlar")
    ],
    [
        KeyboardButton("✍️ Fikr bildirish"),
        KeyboardButton("⚙️ Sozlamalar")
    ]
])


menu_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("🛒 Сделать заказ"),
        KeyboardButton("🛍 Мои заказы")
    ],
    [
        KeyboardButton("📍 Локации")
    ],
    [
        KeyboardButton("✍️ Комментарий"),
        KeyboardButton("⚙️ Настройки")
    ]
])


send_number = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("Telefon raqam yuborish📲", request_contact=True)
    ]
])


send_number_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("Отправить номер телефона📲", request_contact=True)
    ]
])


back = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("⬅️ Ortga")
    ]
])


back_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("⬅️ Назад")
    ]
])


send_location_location_none = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("📍 Joylashuv qo'shish")
    ],
    [
        KeyboardButton("⬅️ Ortga")
    ]
])


send_location = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("📍 Mening joylashuvim", request_location=True)
    ]
])


send_location_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("📍 Мое местонахождение", request_location=True)
    ]
])



def locations_button(user_id):
    all_locations = [[
        KeyboardButton("📍 Joylashuv qo'shish")
    ]]
    
    for locations in db.get_locations(user_id):
        all_locations.append([KeyboardButton(f"{locations[1]}")])
    
    all_locations.append([
        KeyboardButton("⬅️ Ortga")
    ])
    
    result = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=all_locations)
    
    return result


def locations_button_ru(user_id):
    all_locations = [[
        KeyboardButton("📍 Добавить местоположение")
    ]]
    
    for locations in db.get_locations(user_id):
        all_locations.append([KeyboardButton(f"{locations[1]}")])
    
    all_locations.append([
        KeyboardButton("⬅️ Назад")
    ])
    
    result = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=all_locations)
    
    return result


send_location_location_none_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton("📍 Добавить местоположение")
    ],
    [
        KeyboardButton("⬅️ Назад")
    ]
])



def categories_button():
    categories_btn = []

    x = 0
    
    for categories in range(int(len(db.get_categories()) / 2)):
        categories_btn.append([
            KeyboardButton(f"{db.get_categories()[x][0]}"),
            KeyboardButton(f"{db.get_categories()[x + 1][0]}")
        ])
        
        x += 2
    
    categories_btn.append([
        KeyboardButton("⬅️ Ortga")
    ])
    
    result = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=categories_btn)
    
    return result


def categories_button_ru():
    categories_btn = []

    x = 0

    for categories in range(int(len(db.get_categories()) / 2)):
        
        
        categories_btn.append([
            KeyboardButton(f"{to_cyrillic(db.get_categories()[x][0])}"),
            KeyboardButton(f"{to_cyrillic(db.get_categories()[x + 1][0])}")
        ])
        
        x += 2
    
    categories_btn.append([
        KeyboardButton("⬅️ Назад")
    ])
    
    result = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=categories_btn)
    
    return result