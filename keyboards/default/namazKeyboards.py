from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

namazButtons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛁Таҳорат қилиш тартиби'),
            KeyboardButton(text='🧎Намоз'),
        ],
        [
            # KeyboardButton(text='🤲 Саҳарлик & Ифторлик'),
            # KeyboardButton(text='🌏Mинтака'),
        ],
        [
            KeyboardButton(text='🔙Оркага'),
        ],
    ],
    resize_keyboard=True,
)

