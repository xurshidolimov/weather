
import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import city
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 Address='Toshkent',
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        pass

    await message.answer(f"Salom <b>{message.from_user.username}</b> \nOb-havo telegram botiga xush kelibsiz.\n"
                         f"Shaharni tanlang", reply_markup=city)

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{message.from_user.username} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)