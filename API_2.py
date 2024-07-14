import requests
import math
from PIL import Image
from io import BytesIO

# Задаем список точек (широта, долгота)
points = [
    (54.735141, 55.957997),
    (54.735851, 55.952237),
    (54.719234, 55.944169),
    (54.720958, 55.933583)
]

def calculate_distance(point1, point2):
    # Рассчитываем расстояние между двумя точками с помощью формулы гаверсинусов
    radius_earth = 6371  # Радиус Земли в километрах
    lat1, lon1 = math.radians(point1[0]), math.radians(point1[1])
    lat2, lon2 = math.radians(point2[0]), math.radians(point2[1])
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius_earth * c
    return distance

# Определяем длину пути
total_distance = 0
for i in range(len(points) - 1):
    point1 = points[i]
    point2 = points[i + 1]
    distance = calculate_distance(point1, point2)
    total_distance += distance

print(f"Длина пути: {total_distance:.2f} км")

# Отобразим путь на карте с помощью сервиса Yandex Maps
api_key = "01f86158-7ab8-4a36-96b3-aacf7693b5d8"
map_params = {
    'l': 'map',
    'size': '650,450',
    'pt': '~'.join([f'{point[1]},{point[0]},pm2wtl' for point in points]),
    'pl': ','.join([f'{point[1]},{point[0]}' for point in points]),
    'key': api_key
}
map_api_server = "https://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
image = Image.open(BytesIO(response.content))
image.show()
