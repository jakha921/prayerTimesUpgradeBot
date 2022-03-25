from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⏳📅Бугун'),
            KeyboardButton(text='📆Eрта'),
        ],
        [
            KeyboardButton(text='🤲 Саҳарлик & Ифторлик'),
            # KeyboardButton(text='🌏Mинтака'),
        ],
        [
            KeyboardButton(text='🙏Намоз хакида кушимча малумотлар'),
        ],
    ],
    resize_keyboard=True,
)

