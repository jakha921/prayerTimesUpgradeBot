from pprint import pprint
import requests
from bs4 import BeautifulSoup
import random


def get_surah_section():
    surah_section = {}

    url = f'https://namoz.islom.uz/suralar.html'

    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')

    try:
        for el in html.select('main > section'):
            id = el.get('id')[8:]
            title = el.select('h2')[0].text
            audio = 'https://namoz.islom.uz/' + \
                el.select('source')[0].get('src')
            text = el.select('.tarjima__text')[0].text

            surah_section[int(id)] = {
                'title': title,
                'audio': audio,
                'text': text
            }

        # pprint(cleaning_section)
        return surah_section
    except:
        return 'Тахорат хакида малумот топилмади'


def get_surah_id():
    surah_id = {}
    url = f'https://namoz.islom.uz/suralar.html'

    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')

    for el in html.select('main > section'):
        id = el.get('id')[8:]
        title = el.select('h2')[0].text
        surah_id[title] = int(id)
    return surah_id


# get_surah_section()[2]

if __name__ == '__main__':
    pprint(get_surah_id())
