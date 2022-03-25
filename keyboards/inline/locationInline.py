
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

import requests
from bs4 import BeautifulSoup


# callback_data
location_callback = CallbackData('location', 'item_name')


# inline keyboard dict
def get_location():
    url = f'https://islom.uz/'

    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')

    for el in html.select('.custom-select > select'):
        region = el.select('option')

        region = [i.text for i in region]
        id = [i.get('value') for i in el.select('option')]

        id = list(map(int, id))

        location = (dict(zip(region, id)))
    return location


locationParsing = get_location()


# location inline keyboard
locationMenu = InlineKeyboardMarkup(row_width=4)
for key, value in locationParsing.items():
    locationMenu.insert(InlineKeyboardButton(
        text=key, callback_data=location_callback.new(item_name=value)))


if __name__ == '__main__':
    print(locationParsing)
