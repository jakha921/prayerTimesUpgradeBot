from pprint import pprint
import requests
from bs4 import BeautifulSoup


def get_namaz_section():
    namaz_text_section = {}

    response = requests.get('https://namoz.islom.uz/namoz.html')
    html = BeautifulSoup(response.content, 'html.parser')

    try:
        for el in html.select('main > section'):
            id = el.get('id')[8:]
            title = el.select('h2')[0].text
            img = 'https://namoz.islom.uz/' + el.select('img')[0].get('src')
            text = [item.text for item in el.select('p')]
            text = '\n'.join(text)

            if el.select('.text__block'):
                translated_text = [item.text for item in el.select('.tarjima__text')]
                audio_text = [item.text for item in el.select('.audio__text')]
                arabic_text = [item.text for item in el.select('.arabic__text')]
                audio_text = '\n'.join(audio_text)
                translated_text = '\n'.join(translated_text)
                arabic_text = '\n'.join(arabic_text)
            else:
                audio_text = None
                translated_text = None
                arabic_text = None

            if el.select('audio > source'):
                mp3 = ['https://namoz.islom.uz/' + item.get('src')
                       for item in el.select('audio > source')]
            else:
                mp3 = None

            # print(f"{id} {mp3}")
            # print(type(audio_text))

            namaz_text_section[id] = {
                'title': title,
                'img': img,
                'text': text,
                'audio_text': audio_text,
                # 'translated_text': translated_text,
                'arabic_text': arabic_text,
                'mp3': mp3,
            }

        # pprint(namaz_text_section)
        return namaz_text_section
    except:
        return 'Тахорат хакида малумот топилмади'


if __name__ == '__main__':
    print(get_namaz_section())
