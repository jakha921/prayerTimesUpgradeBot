import logging
from aiogram import types

from parsings.ramadanText import saxarlik, iftar

from loader import dp

# back
# @dp.callback_query_handler(text="back")
# async def get_back(call: types.CallbackQuery):
#     # callback_data = call.data
#     # logging.info(f'{callback_data=}')
#     # logging.info(f'{call.from_user.id=}')
#     await call.message.edit_reply_markup(reply_markup=ramadanMenu)
#     await call.answer()


@dp.callback_query_handler(text="cахарлик")
async def get_sahar(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(saxarlik)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="ифторлик")
async def get_iftar(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(iftar)
    await call.answer(cache_time=60)


if __name__ == '__main__':
    print(saxarlik)