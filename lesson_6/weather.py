import geocoder
import requests
from googletrans import Translator
from bs4 import BeautifulSoup
from datetime import date


URL = "https://sinoptik.ua/погода-"


def scraping_weather(city, data):
    web_page = requests.get(f'{URL}{city}/{data}')
    if web_page.status_code == 200:
        soup = BeautifulSoup(web_page.content, 'html.parser')
        weather = soup.find('div', class_='main loaded')
        weather_description = weather.find('div')['title']
        temp_min = weather.find('div', class_='min').text
        temp_max = weather.find('div', class_='max').text
        return f'{city}\n{weather_description}\nТемпература: {temp_min} - {temp_max}'
    else:
        print("Что-то пошло не так!")


if __name__ == "__main__":

    try:
        translator = Translator()
        g = geocoder.ip('me')
        location = geocoder.osm(g.latlng, method='reverse')
        translation = translator.translate(location.json['city'], dest="ru")
        my_location = translation.text
        result = scraping_weather(my_location, date.today())
        print(result)
    except AttributeError:
        print('Не удалось установить ваше местоположение.')

    while True:
        user_option = input('Хотите узнать погоду в другом городе ? Д/Н\n')
        if user_option in ["Д", "д", "Y", "y"]:
            user_city = input('Укажите город: ')
            user_data = input("Введите дату в формате гггг-мм-дд: ")
            result = scraping_weather(user_city, user_data)
            if result:
                print(result)
            else:
                print('Нет данных о погоде.')
        if user_option in ["Н", "н", "N", "n"]:
            break
