from datetime import datetime
import requests
from bs4 import BeautifulSoup


# get by date
def get_prayer_times(currentMonth, *currentDay):
    """Return the time of prayer for today"""
    url = f'https://islom.uz/vaqtlar/14/{currentMonth}'

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    body = soup.find('tbody')
    head = soup.find('thead')

    try:
        for data in currentDay:
            day = body.find_all('td')[(data-1)*9+1].text
            month = head.find_all('th')[1].text
            prayer_day = body.find_all('td')[(data-1)*9+2].text
            Fajr = body.find_all('td')[(data-1)*9+3].text
            Sunrise = body.find_all('td')[(data-1)*9+4].text
            Dhuhr = body.find_all('td')[(data-1)*9+5].text
            Asr = body.find_all('td')[(data-1)*9+6].text
            Maghrib = body.find_all('td')[(data-1)*9+7].text
            Isha = body.find_all('td')[(data-1)*9+8].text

            msg = f'{day} {month.title()} {prayer_day}\n'
            msg += f'*🌇Тонг(Саҳарлик) : {Fajr}*\n'
            msg += f'Қуёш : {Sunrise}\n'
            msg += f'Пешин : {Dhuhr}\n'
            msg += f'Аср : {Asr}\n'
            msg += f'*🌃Шом(Ифтор) : {Maghrib}*\n'
            msg += f'Хуфтон : {Isha}\n'

            return msg
    except:
        return 'Маълумот топилмади!'


def get_prayer_times_for_today():
    try:
        today = datetime.now().day
        currentMonth = datetime.now().month
        return get_prayer_times(currentMonth, today)
    except:
        return 'Бугун учун малумот топилмади!'

def get_prayer_times_for_tomorrow():
    try:
        today = datetime.now().day
        currentMonth = datetime.now().month
        if currentMonth == 2 and today == 28:
            return get_prayer_times(currentMonth+1, 1)
        elif currentMonth == 3 and today == 31:
            return get_prayer_times(currentMonth+1, 1)
        elif currentMonth == 4 and today == 30:
            return get_prayer_times(currentMonth+1, 1)
        elif currentMonth == 5 and today == 31:
            return get_prayer_times(currentMonth+1, 1)
        elif currentMonth == 6 and today == 30:
            return get_prayer_times(currentMonth+1, 1)
        elif currentMonth == 7 and today == 31:
            return get_prayer_times(currentMonth+1, 1)
        else:
            return get_prayer_times(currentMonth, today+1)
    except:
        return 'Ертанки кун учун малумот топилмади!'


if __name__ == '__main__':
    print(get_prayer_times_for_tomorrow())
