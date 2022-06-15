from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

# from aiogram import Bot
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor



# @dp.message_handler()
# async def echo_send(message: types.Message):

async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()


from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

    # ответ туда куда написал
    # await message.answer(message.text)

    # ответ с циатой
    # await message.reply(message.text)

    # ответ в личку
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)