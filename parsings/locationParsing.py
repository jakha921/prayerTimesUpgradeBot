import requests
from bs4 import BeautifulSoup


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

        # print(location)vb
    return location


if __name__ == '__main__':
    print(get_location())
