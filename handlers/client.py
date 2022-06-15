from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db



# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать, рады Вас видеть!\nВыберете пункт меню:', reply_markup=kb_client)
        await message.delete()
    except:
        await message.answer('Общение с ботом через ЛС, напишите ему:\n@dipeshot_bot ')
        # await message.delete()

# @dp.message_handler(commands=[''])
async def pizza_open_command(message : types.Message):
    # await message.delete()
    await bot.send_message(message.from_user.id, '<b>Режим работы:</b>\nВс-Чт с 9:00 до 20:00\nПт-Сб с 10:00 до 23:00', parse_mode=types.ParseMode.HTML)
    print('Пользователь запросил режим работы')

# @dp.message_handler(commands=['place'])
async def pizza_place_command(message : types.Message):
    # await message.delete()
    await bot.send_message(message.from_user.id, 'ул. Маршала Жукова 3')#,  reply_markup=ReplyKeyboardRemove()) - удаление клавиатуры после нажатия кнопки
    print('Пользователь запросил адресс')

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)
    print('Пользователь запросил меню')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Время_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])