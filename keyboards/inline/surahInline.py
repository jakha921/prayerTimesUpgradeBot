
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from parsings.surahParsing import get_surah_id


# callback_data
surah_callback = CallbackData('surah', 'item_name')


surahParsing = get_surah_id()


# location inline keyboard
surahsMenu = InlineKeyboardMarkup(row_width=4)
for key, value in surahParsing.items():
    surahsMenu.insert(InlineKeyboardButton(
        text=key, callback_data=surah_callback.new(item_name=value)))


if __name__ == '__main__':
    print(surahParsing)
