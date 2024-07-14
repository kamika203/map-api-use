# 7. Напишите программу, которая поможет вам определить, в каком районе
# находится заданный адрес. Адрес передаётся в командной строке.
#
# Подсказка. По введённому адресу надо сперва найти координаты,
# а с полученными координатами надо «сходить» в геокодер,
# указав в параметре kind значение district (район).

import sys
import requests

if len(sys.argv) == 1:
    print("No arguments")
else:
    address=' '.join(sys.argv[1:])
    print(address)
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
    params = {
        "apikey": api_key,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(geocode_url, params=params)
    data = response.json()
    # Извлечение координат из ответа
    try:
        point = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        longitude, latitude = map(float, point.split())
    except (KeyError, IndexError):
        print("Не удалось получить координаты для адреса.")

    # Запрос к геокодеру для получения информации о районе
    reverse_geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": api_key,
        "geocode": f"{longitude},{latitude}",
        "kind": "district",
        "format": "json"
    }
    response = requests.get(reverse_geocode_url, params=params)
    data = response.json()
    # Извлечение информации о районе из ответа
    try:
        district = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]
        print(f"Район: {district}")
    except (KeyError, IndexError):
        print("Не удалось определить район для заданного адреса.")
