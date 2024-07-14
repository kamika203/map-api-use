# Напишите программу, считающую (приближённо) расстояние от вашего дома до университета
#
# Адреса БашГУ и дома вводятся пользователем в консоль после запуска программы,
# а в качестве метрики расстояния вам нужно использовать декартову метрику
# на градусной сетке, считая 1 градус по широте равным 111 километрам,
# а отношение градуса широты и градуса долготы, равным косинусу широты.


import math
import requests

# Определяем функцию, считающую расстояние между двумя точками, заданными координатами
def lonlat_distance(a, b):

    degree_to_meters_factor = 111 * 1000 # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance

def get_coord(adress):
    search_params["text"]=adress
    response = requests.get(search_api_server, params=search_params)
    json_response = response.json()
    point=json_response['features'][0]['geometry']['coordinates']

    return (float(point[0]),float(point[1]))

a_Univer=input("Введите адрес университета: ")
a_home=input("Введите ваш адрес: ")

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

search_params = {
    "apikey": api_key,
    "text": '',
    "lang": "ru_RU"
}

#координаты вуза
a=get_coord(a_Univer)
#координаты дома
b=get_coord(a_home)

dis=lonlat_distance(a,b)
print("Расстояние от вашего дома до университета: ",dis)
