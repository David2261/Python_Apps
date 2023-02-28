import time
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Token
from decouple import config

TOKEN = config("API_TELEGRAM_TOKEN", default='')
MSG = "Введите номер телефона {}: "

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
	user_id = message.from_user.id
	user_name = message.from_user.first_name
	user_full_name = message.from_user.full_name
	logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

	await message.reply(f"Привет! {user_full_name}")

	await bot.send_message(user_id, MSG.format(user_name))

	n = await state.get_data()
	name = n['phone']

if __name__ == '__main__':
	executor.start_polling(dp)

