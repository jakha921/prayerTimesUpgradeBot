import requests
from bs4 import BeautifulSoup


def get_cleaning_section():
    cleaning_section = {}

    url = f'https://namoz.islom.uz/'

    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')

    try:
        for el in html.select('main > section'):
            id = el.get('id')[-1]
            title = el.select('h2')[0].text
            img = url + el.select('img')[0].get('src')
            text = [item.text for item in el.select('p')]
            text = '\n'.join(text)

            cleaning_section[id] = {
                'title': title,
                'img': img,
                'text': text
            }
        return cleaning_section
    except:
        return 'Тахорат хакида малумот топилмади'


if __name__ == '__main__':
    print(get_cleaning_section())
