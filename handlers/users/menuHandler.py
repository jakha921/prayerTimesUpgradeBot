import logging
from aiogram import types

from keyboards.inline.locationInline import locationMenu, location_callback
from keyboards.inline.ramadanInline import ramadanMenu
from keyboards.default.namazKeyboards import namazButtons
from parsings.prayerTimes import get_prayer_times_for_today, get_prayer_times_for_tomorrow

from loader import dp


@dp.message_handler(text='⏳📅Бугун')
async def get_today_prayer_time(message: types.Message):
    # logging.info(message)
    today = get_prayer_times_for_today()
    await message.answer(f'Бугун :\n{today} ', parse_mode="Markdown")


@dp.message_handler(text='📆Eрта')
async def get_tommorow_prayer_time(message: types.Message):
    # logging.info(message)
    tommorow = get_prayer_times_for_tomorrow()
    await message.answer(f'Ертага :\n{tommorow} ', parse_mode="Markdown")


@dp.message_handler(text='🤲 Саҳарлик & Ифторлик')
async def get_ramadan(message: types.Message):
    # logging.info(message)
    await message.answer(f'Танглан: ', reply_markup=ramadanMenu)


@dp.message_handler(text='🌏Mинтака')
async def get_location_inline_keyboards(message: types.Message):
    # logging.info(message)
    await message.answer("Choose section:", reply_markup=locationMenu)


@dp.message_handler(text='🙏Намоз хакида кушимча малумотлар')
async def get_ramadan(message: types.Message):
    # logging.info(message)
    await message.answer('Тангланг', reply_markup=namazButtons)


# if __name__ == '__main__':
#     print(locationParsing)
