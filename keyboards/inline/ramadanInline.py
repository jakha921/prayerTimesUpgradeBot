
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# inline keyboard
ramadanMenu = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Саҳарлик', callback_data='cахарлик'),
        ],
        [
            InlineKeyboardButton(text='Ифторлик', callback_data='ифторлик'),
        ],
    ]
    )

back = InlineKeyboardButton(text='⬅️Back', callback_data='back')
