
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from parsings.locationParsing import get_location


# callback_data
location_callback = CallbackData('location', 'item_name')


locationParsing = get_location()


# location inline keyboard
locationMenu = InlineKeyboardMarkup(row_width=4)
for key, value in locationParsing.items():
    locationMenu.insert(InlineKeyboardButton(
        text=key, callback_data=location_callback.new(item_name=value)))


if __name__ == '__main__':
    print(locationParsing)
