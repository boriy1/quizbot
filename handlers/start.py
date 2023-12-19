from loader import dp, bot
from aiogram import types
from database import database as db
from states.register import Register
from keyboards.inline.lang import lang
from keyboards.default.menu import send_number, menu, send_number_ru, menu_ru
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    db.create_table()
    
    await state.finish()
    
    if not db.get_user(message.from_id):
        await Register.lang.set()
        await message.answer("<b>Tilni tanlang!</b>", parse_mode='html', reply_markup=lang)
    else:
        user = db.get_user(message.from_id)
        if user[1] == 'uz':
            await message.answer(f"<b>Salom {message.from_user.first_name}</b>", parse_mode='html')
            await message.answer("<b>Kerakli bo'limni tanlang!</b>", parse_mode='html', reply_markup=menu)
        else:
            await message.answer(f"<b>Привет {message.from_user.first_name}</b>", parse_mode='html')
            await message.answer("<b>Выбирайте нужный раздел!</b>", parse_mode='html', reply_markup=menu_ru)


@dp.callback_query_handler(state=Register.lang)
async def set_lang(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'uz':
        await state.update_data({'lang': 'uz'})
        await bot.send_message(chat_id=call.from_user.id, text="<b>Telefon raqamingizni yuboring!</b>", parse_mode='html', reply_markup=send_number)
        await Register.phone_number.set()
    else:
        await state.update_data({'lang': 'ru'})
        await bot.send_message(chat_id=call.from_user.id, text="<b>Отправьте свой номер телефона!</b>", parse_mode='html', reply_markup=send_number_ru)
        await Register.phone_number.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Register.phone_number)
async def get_contact(message: types.Message, state: FSMContext):
    data = await state.get_data()
    
    if data['lang'] == 'uz':
        await message.answer("<b>Siz muvvafaqiyatli ro'yxatdan o'tdingiz!</b>", parse_mode='html', reply_markup=menu)
    else:
        await message.answer("<b>Вы успешно зарегистрировались!</b>", parse_mode='html', reply_markup=menu)
        
    db.add_user(message.from_id, message.contact.phone_number, data['lang'])
    await state.finish()
