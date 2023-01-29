from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db import Database
import functions as fc
from data.config import token

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
db = Database('database.db')


@dp.message_handler(commands='start')
async def start_msg(message: types.Message):
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEHfWZj1Vq0e-Uhlcz1sIilN3z7M6RsOQACAQEAAladvQoivp8OuMLmNC0E')


@dp.message_handler()
async def msg(message: types.Message):
    answer_id = fc.recognize_question(message.text, db.get_questions())
    await bot.send_message(message.from_user.id, db.get_answer(answer_id))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
