from aiogram import types

from keyboards.inline.locationInline import location_callback



# 🌏Mинтака Inline keyboard
# @dp.callback_query_handler(location_callback.filter(item_name='Навоий'))
# async def get_location(call: types.CallbackQuery):
#     # # await call.message.delete()
#     # callback_data = call.data
#     # logging.info(f'{callback_data=}')
#     # logging.info(f'{call.from_user.id=}')
#     await call.answer('Сизни миткангиз Навоий деб танланди!', cache_time=60, show_alert=True)