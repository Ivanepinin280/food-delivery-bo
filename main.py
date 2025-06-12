from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

TOKEN = "8135782856:AAESvjgav4PdsN1ESJMUwUUszMpFrJy4450"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="Открыть доставку еды",
            web_app=WebAppInfo(url="https://ivanepinin280.github.io/food-delivery/")
        )
    )
    await message.answer("Нажми кнопку, чтобы открыть приложение:", reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dp)
