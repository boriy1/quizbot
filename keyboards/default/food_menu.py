from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database import database as db
from functions.transliterate import to_cyrillic


def find_food_by_category(foods):
    foods_list = [[
        KeyboardButton("⬅️ Ortga")
    ]]
    for foods_button in foods:
        foods_list.append([
            KeyboardButton(f"{foods_button[0]} - {foods_button[1]} so'm")
        ])
    
    result = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=foods_list)

    return result



def find_food_by_category_ru(foods):
    foods_list = [[
        KeyboardButton("⬅️ Назад")
    ]]
    for foods_button in foods:
        foods_list.append([
            KeyboardButton(f"""{to_cyrillic(foods_button[0])} - {to_cyrillic(str(foods_button[1]))} {to_cyrillic("sum")}""")
        ])
    
    result = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=foods_list)

    return result