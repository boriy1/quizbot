from loader import dp, bot
from aiogram import types
from geopy.geocoders import Nominatim

from database import database as db
from states.send_comment import SendComment, SendCommentRu
from states.location import AddLocation, AddLocationRu
from keyboards.inline.lang import lang
from keyboards.inline.settings import settings, settings_ru
from keyboards.default.menu import menu, menu_ru, back, back_ru, send_location_location_none, locations_button, send_location, locations_button_ru, send_location_location_none_ru, send_location_ru, categories_button, categories_button_ru
from keyboards.default.food_menu import find_food_by_category, find_food_by_category_ru
from aiogram.dispatcher import FSMContext
from functions.transliterate import to_latin, to_cyrillic
from keyboards.inline.buy_food import buy_food, buy_food_ru
from keyboards.inline.check import check, check_ru
from states.add_product_to_cart import AddProductToCart, AddProductToCartRu
from states.confirm import Confirm, ConfirmRu



@dp.message_handler(text=['🛒 Buyurtma qilish'])
async def get_categories_handler(message: types.Message, state: FSMContext):
    await message.answer("<b>Kerakli bo'limni tanlang!</b>", parse_mode='html', reply_markup=categories_button())


@dp.message_handler(text=['✍️ Fikr bildirish'])
async def send_comment(message: types.Message, state: FSMContext):
    await message.answer(f"<b>Fikringizni yozing!</b>", reply_markup=back)
    await SendComment.text.set()


@dp.message_handler(text=['⬅️ Ortga'], state="*")
async def cancel_comment(message: types.Message, state: FSMContext):
    await message.answer(f"<b>Kerakli bo'limni tanlang!</b>", reply_markup=menu)
    await state.finish()


@dp.message_handler(state=SendComment.text)
async def get_text_comment(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=-1002060801446, text=f"""<b>User: {message.from_user.first_name}\nUsername: @{message.from_user.username}\nLanguage: O'zbekcha\n\n{message.text}</b>""", parse_mode='html')
    await message.answer("<b>Fikr bildirganingiz uchun raxmat!</b>", parse_mode='html', reply_markup=menu)
    await state.finish()
    
    
@dp.message_handler(text=['⚙️ Sozlamalar'])
async def settings_menu(message: types.Message, state: FSMContext):
    await message.answer("<b>Sozlamalar!</b>", parse_mode='html', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"<b>Telefon raqam: {db.get_user(message.from_id)[2]}\nTil: O'zbekcha🇺🇿</b>", reply_markup=settings)


@dp.message_handler(text=['📍 Joylashuvlar'])
async def get_locations_handler(message: types.Message, state: FSMContext):
    if not db.get_locations(message.from_id):
        await message.answer("<b>Joylashuvlar mavjud emas!</b>", parse_mode='html', reply_markup=send_location_location_none)
    else:
        await message.answer("<b>Joylashuvlaringiz!</b>", reply_markup=locations_button(message.from_id), parse_mode='html')
        

@dp.message_handler(text=['📍 Joylashuv qo\'shish'])
async def add_locations_handler(message: types.Message, state: FSMContext):
    await AddLocation.location.set()
    await message.answer("<b>Joylashuv yuboring!</b>", parse_mode='html', reply_markup=send_location)
    

@dp.message_handler(text=['🛍 Buyurtmalarim'])
async def orders_handler(message: types.Message, state: FSMContext):
    products_all = db.get_products_(message.from_id)
    
    text = "<b>🛍Savat\n\n"
    x = 0
    price = 0
    
    for products in products_all:
        x += 1
        text += f"{x}. {products[1]} - {products[2]} so'm\n"
        price += products[2]
    
    text += f"\nJami: {price} so'm</b>"
    
    if not x == 0:
        await message.answer("<b>Buyurtmalaringiz!</b>", parse_mode='html', reply_markup=types.ReplyKeyboardRemove())
        await message.answer(f"{text}", parse_mode='html', reply_markup=check)
        await Confirm.check.set()
        await state.update_data({'products': text})
    else:
        await message.answer(f"<b>Savat bo'sh</b>", parse_mode='html', reply_markup=menu)
        














# RU
@dp.message_handler(text=['🛍 Мои заказы'])
async def orders_handler(message: types.Message, state: FSMContext):
    products_all = db.get_products_(message.from_id)
    
    text = "<b>🛍 Корзина\n\n"
    x = 0
    price = 0
    
    for products in products_all:
        x += 1
        text += f"{x}. {to_cyrillic(products[1])} - {products[2]} сум\n"
        price += products[2]
    
    text += f"\nВсего: {price} сум</b>"
    
    if not x == 0:
        await message.answer("<b>Ваши заказы!</b>", parse_mode='html', reply_markup=types.ReplyKeyboardRemove())
        await message.answer(f"{text}", parse_mode='html', reply_markup=check_ru)
        await ConfirmRu.check.set()
        await state.update_data({'products': text})
    else:
        await message.answer(f"<b>Корзина пуста</b>", parse_mode='html', reply_markup=menu_ru)
        


@dp.message_handler(text=['🛒 Сделать заказ'])
async def get_categories_handler_ru(message: types.Message, state: FSMContext):
    await message.answer("<b>Выберите нужный раздел!</b>", parse_mode='html', reply_markup=categories_button_ru())


@dp.message_handler(text=['✍️ Комментарий'])
async def send_comment_ru(message: types.Message, state: FSMContext):
    await message.answer(f"<b>Напишите свое мнение!</b>", reply_markup=back_ru)
    await SendCommentRu.text.set()


@dp.message_handler(text=['⬅️ Назад'], state="*")
async def cancel_comment_ru(message: types.Message, state: FSMContext):
    await message.answer(f"<b>Выбирайте нужный раздел!</b>", reply_markup=menu_ru)
    await state.finish()



@dp.message_handler(text=['📍 Локации'])
async def get_locations_handler_ru(message: types.Message):
    if not db.get_locations(message.from_id):
        await message.answer("<b>Места недоступны!</b>", parse_mode='html', reply_markup=send_location_location_none_ru)
    else:
        await message.answer("<b>Ваши местоположения!</b>", reply_markup=locations_button_ru(message.from_id), parse_mode='html')



@dp.message_handler(state=SendCommentRu.text)
async def get_text_comment_ru(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=-1002060801446, text=f"""<b>User: {message.from_user.first_name}\nUsername: @{message.from_user.username}\nLanguage: Ruscha\n\n{message.text}</b>""", parse_mode='html')
    await message.answer("<b>Спасибо за ваш комментарий!</b>", parse_mode='html', reply_markup=menu_ru)
    await state.finish()
        

@dp.message_handler(text=['📍 Добавить местоположение'])
async def add_locations_handler_ru(message: types.Message, state: FSMContext):
    await AddLocationRu.location.set()
    await message.answer("<b>Отправить местоположение!</b>", parse_mode='html', reply_markup=send_location_ru)


@dp.message_handler(text=['⚙️ Настройки'])
async def settings_menu_ru(message: types.Message, state: FSMContext):
    await message.answer("<b>Настройки!</b>", parse_mode='html', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"<b>Номер телефона: {db.get_user(message.from_id)[2]}\nЯзык: Русский🇷🇺</b>", reply_markup=settings_ru)


@dp.callback_query_handler(text=['confirmed'], state=Confirm.check)
async def confirm_order_handler(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=call.from_user.id, text=f"<b>Qaysi manzilga yetkazib berishimizni xoxlaysiz?</b>", reply_markup=locations_button(call.from_user.id), parse_mode='html')
    await Confirm.location.set()


@dp.callback_query_handler(text=['confirmed'], state=ConfirmRu.check)
async def confirm_order_handler(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=call.from_user.id, text=f"<b>На какой адрес вы хотите, чтобы мы доставили?</b>", reply_markup=locations_button_ru(call.from_user.id), parse_mode='html')
    await ConfirmRu.location.set()
    

@dp.callback_query_handler(text=['clear'], state=ConfirmRu.check)
async def clear(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=call.from_user.id, text=f"<b>Корзина опустела!</b>", reply_markup=menu_ru, parse_mode='html')
    await state.finish()
    db.delete_cart(call.from_user.id)


@dp.callback_query_handler(text=['clear'], state=Confirm.check)
async def clear(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=call.from_user.id, text=f"<b>Savat bo'shatildi!</b>", reply_markup=menu, parse_mode='html')
    await state.finish()
    db.delete_cart(call.from_user.id)


@dp.message_handler(state=Confirm.location)
async def location_handler(message: types.Message, state: FSMContext):
    msg = message.text
    send_location = False
    
    for locations in db.get_locations(message.from_id):
        if msg == locations[1]:
            send_location = True
            lon = float(locations[2])
            lat = float(locations[3])
            
    if send_location:
        data = await state.get_data()
        
        await bot.send_message(text=f"<b>Buyurtma qabul qilindi!</b>", parse_mode='html', chat_id=message.from_id, reply_markup=menu)
        await bot.send_location(chat_id=-1002060801446, latitude=lat, longitude=lon)
        await bot.send_message(chat_id=-1002060801446, text=f"<b>{data['products']}\nTelefon raqam: {db.get_user(message.from_id)[2]}\nLocation: {msg}</b>", parse_mode='html')
        db.delete_cart(message.from_id)
        await state.finish()
        

@dp.message_handler(state=ConfirmRu.location)
async def location_handler(message: types.Message, state: FSMContext):
    msg = message.text
    send_location = False
    
    for locations in db.get_locations(message.from_id):
        if msg == locations[1]:
            send_location = True
            lon = float(locations[2])
            lat = float(locations[3])
            
    if send_location:
        data = await state.get_data()
        
        await bot.send_message(text=f"<b>Заказ принят!</b>", parse_mode='html', chat_id=message.from_id, reply_markup=menu_ru)
        await bot.send_location(chat_id=-1002060801446, latitude=lat, longitude=lon)
        await bot.send_message(chat_id=-1002060801446, text=f"<b>{data['products']}\nTelefon raqam: {db.get_user(message.from_id)[2]}\nLocation: {msg}</b>", parse_mode='html')
        db.delete_cart(message.from_id)
        await state.finish()



@dp.callback_query_handler(text=['set_lang'])
async def set_lang(call: types.CallbackQuery):
    if db.get_user(call.from_user.id)[1] == 'uz':
        db.update_lang(call.from_user.id, 'ru')
        await call.answer("Язык был изменен!")
        await bot.send_message(chat_id=call.from_user.id, text=f"<b>Выбирайте нужный раздел!</b>", parse_mode='html', reply_markup=menu_ru)
    else:
        db.update_lang(call.from_user.id, 'uz')
        await call.answer("Til o'zgartirildi!")
        await bot.send_message(chat_id=call.from_user.id, text=f"<b>Kerakli bo'limni tanlang!</b>", parse_mode='html', reply_markup=menu)


@dp.callback_query_handler(text=['back', 'back_ru'])
async def back_callback(call: types.CallbackQuery):
    if call.data == 'back':
        await bot.send_message(chat_id=call.from_user.id, text="<b>Kerakli bo'limni tanlang!</b>", parse_mode='html', reply_markup=menu)
    else:
        await bot.send_message(chat_id=call.from_user.id, text="<b>Выберите нужный раздел!</b>", parse_mode='html', reply_markup=menu_ru)
    


@dp.callback_query_handler(text=['add_cart'], state=AddProductToCart.check)
async def add_cart_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    title = data['product']
    price = data['price']
    
    db.add_product_to_cart(call.from_user.id, title, price)
    await bot.send_message(chat_id=call.from_user.id, text=f"<b>{title} savatga qo'shildi✅</b>", parse_mode='html', reply_markup=categories_button())
    await state.finish()
    
    
@dp.callback_query_handler(text=['add_cart_ru'], state=AddProductToCartRu.check)
async def add_cart_handler_ru(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    title = data['product']
    price = data['price']
    
    db.add_product_to_cart(call.from_user.id, title, price)
    await bot.send_message(chat_id=call.from_user.id, text=f"<b>{to_cyrillic(title)} добавлено в корзину✅</b>", parse_mode='html', reply_markup=categories_button_ru())
    await state.finish()



@dp.message_handler(state=AddLocation.location, content_types=[types.ContentType.LOCATION])
async def add_locations_state_handler(message: types.Message, state: FSMContext):
    longitude = str(message.location.longitude)
    latitude = str(message.location.latitude)
    
    geolocator = Nominatim(user_agent="user") # API
    location = geolocator.geocode(latitude + "," + longitude) # Location
    
    db.add_location(message.from_id, str(location), longitude, latitude)
    await message.answer("<b>Joylashuv qo'shildi!</b>", parse_mode='html', reply_markup=locations_button(message.from_id))
    await state.finish()
    


@dp.message_handler(lambda message: message.text)
async def locations_button_handler_ru(message: types.Message, state: FSMContext):
    msg = message.text
    send_location = False
    
    
    for locations in db.get_locations(message.from_id):
        if msg == locations[1]:
            send_location = True
            lon = float(locations[2])
            lat = float(locations[3])
            
    if send_location:
        await bot.send_location(chat_id=message.from_id, longitude=lon, latitude=lat, reply_markup=back_ru)
        
        
    for categories in db.get_categories():
        if not message.text.isascii():
            msg = to_latin(message.text)
            if categories[0] == msg:
                await message.answer("<b>Выберите нужный раздел!</b>", parse_mode='html', reply_markup=find_food_by_category_ru(db.get_products(msg)))
        else:
            if categories[0] == message.text:
                await message.answer(f"<b>Kerakli bo'limni tanlang!</b>", parse_mode='html', reply_markup=find_food_by_category(db.get_products(msg)))
              
                
    for product in db.get_products_all():
        splitted_msg = message.text.split(" - ")
        if not message.text.isascii():
            msg = to_latin(splitted_msg[0])
            if product[0] == msg:
                await message.answer(f"<b>О продукте</b>", reply_markup=types.ReplyKeyboardRemove())
                await message.answer(f"<b>- {to_cyrillic(product[0])} -\n\n🌮Категория: {to_cyrillic(product[3])}\n💸Расходы: {product[1]} сум\nℹ️О продукте: {to_cyrillic(product[2])}</b>", parse_mode='html', reply_markup=buy_food_ru)
                await AddProductToCartRu.check.set()
                await state.update_data({'product': product[0], 'price': int(product[1])})
        else:
            if product[0] == splitted_msg[0]:
                await message.answer(f"<b>Maxsulot haqida</b>", reply_markup=types.ReplyKeyboardRemove())
                await message.answer(f"<b>- {product[0]} -\n\n🌮Kategoriya: {product[3]}\n💸Narxi: {product[1]} so'm\nℹ️Mahsulot haqida: {product[2]}</b>", parse_mode='html', reply_markup=buy_food)
                await AddProductToCart.check.set()
                await state.update_data({'product': product[0], 'price': int(product[1])})
    
    
    
    
@dp.message_handler(lambda message: message.text)
async def locations_button_handler(message: types.Message, state: FSMContext):
    msg = message.text
    send_location = False
    
    
    for locations in db.get_locations(message.from_id):
        if msg == locations[1]:
            send_location = True
            lon = float(locations[2])
            lat = float(locations[3])
            
    if send_location:
        await bot.send_location(chat_id=message.from_id, longitude=lon, latitude=lat, reply_markup=back)

        

    
    
@dp.message_handler(state=AddLocationRu.location, content_types=[types.ContentType.LOCATION])
async def add_locations_state_handler_ru(message: types.Message, state: FSMContext):
    longitude = str(message.location.longitude)
    latitude = str(message.location.latitude)
    
    geolocator = Nominatim(user_agent="user") # API
    location = geolocator.geocode(latitude + "," + longitude) # Location
    
    db.add_location(message.from_id, str(location), longitude, latitude)
    await message.answer("<b>Местоположение добавлено!</b>", parse_mode='html', reply_markup=locations_button_ru(message.from_id))
    await state.finish()