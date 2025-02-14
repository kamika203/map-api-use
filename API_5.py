import requests
from PIL import Image
from io import BytesIO

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

# add=input("широта ")
# addr=input("долгота ")
# address_ll = "{0},{1}".format(add, addr)
address_ll=input("Адрес ")

search_params = {
    "apikey": api_key,
    "text": address_ll,
    "lang": "ru_RU",
}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()
point=json_response['features'][0]['geometry']['coordinates']
address_ll = "{0},{1}".format(point[0], point[1])

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)

# Преобразуем ответ в json-объект
json_response = response.json()

# Получаем первую найденную организацию.
organization = json_response["features"][0]
# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]

# Получаем координаты ответа.
point = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(point[0], point[1])
#delta = "0.01"#размеры

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": address_ll,
    #"spn": ",".join([delta, delta]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": "{0},pm2dgl".format(org_point)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

# Read the image from the response content
image = Image.open(BytesIO(response.content))

# Show the image
image.show()
