import logging
from aiogram import types
import asyncio

from keyboards.default.namazKeyboards import namazButtons
from keyboards.default.menuKeyboards import menuStart
from parsings.cleaningParsing import get_cleaning_section
from parsings.prayerParsing import get_namaz_section

from keyboards.inline.surahInline import surahsMenu



from loader import dp


@dp.message_handler(text='🛁Таҳорат қилиш тартиби')
async def get_prayer(message: types.Message):
    # logging.info(message)
    prayer = get_cleaning_section()
    for id, value in prayer.items():
        await message.answer_animation(value["img"], caption=f'<b>{value["title"]}</b>\n\n{value["text"]}')
        await asyncio.sleep(5)


@dp.message_handler(text='🧎Намоз')
async def get_prayer(message: types.Message):
    # logging.info(message)
    namaz = get_namaz_section()
    for id, value in namaz.items():
        animation = f'<b>{value["title"]}</b>\n\n{value["text"]}'
        audio_arabic = f"{value['arabic_text']}"
        audio_text = f"{value['audio_text']}"

        if value['img'] is not None:
            try:
                await message.answer_animation(value["img"], caption=animation)
            except:
                await message.answer_animation(value["img"])
                await message.answer(animation.strip())

        if value['mp3'] is not None:
            for audio in value['mp3']:
                try:
                    await message.answer_voice(audio, caption=f'{audio_arabic}\n {audio_text}')
                except:
                    await message.answer_voice(audio, caption=audio_arabic)
                    # await message.answer(audio_text)

        await asyncio.sleep(4)


@dp.message_handler(text='📖 Суралар')
async def get_prayer(message: types.Message):
    logging.info(message)
    await message.answer('Бош менюга', reply_markup=surahsMenu)


@dp.message_handler(text='🔙Оркага')
async def get_tommorow_prayer_time(message: types.Message):
    # logging.info(message)
    await message.answer('Бош менюга', reply_markup=menuStart)
