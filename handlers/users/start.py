from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.InlineKeyboards import tilmenu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Til tanlang:\n"
                         f"Привет, {message.from_user.full_name}! Выберите язык:", reply_markup=tilmenu)
