import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyboards import menuStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # logging.info(message)
    
    msg = f"Салом, {message.from_user.full_name}!\n"
    msg += f"Мен Намоз ва Руза вактиларини айтувчи бот ман\n\n"
    # msg += f"Mентакангизни танланг:"
    msg += 'Хозирча Навои шахар учун вактларни курсата оламан' 
    
    await message.answer(msg, reply_markup=menuStart)

