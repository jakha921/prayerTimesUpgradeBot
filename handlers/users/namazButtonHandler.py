import logging
from aiogram import types
import asyncio

from keyboards.default.namazKeyboards import namazButtons
from keyboards.default.menuKeyboards import menuStart
from parsings.cleaningParsing import get_cleaning_section

from loader import dp


@dp.message_handler(text='🛁Таҳорат қилиш тартиби')
async def get_prayer(message: types.Message):
    # logging.info(message)
    prayer = get_cleaning_section()
    for id, value in prayer.items():
        await message.answer_animation(value["img"], caption=f'<b>{value["title"]}</b>\n\n{value["text"]}')
        await asyncio.sleep(5)


@dp.message_handler(text='🔙Оркага')
async def get_tommorow_prayer_time(message: types.Message):
    # logging.info(message)
    await message.answer('Бош менюга', reply_markup=menuStart)
