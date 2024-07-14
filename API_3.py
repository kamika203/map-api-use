import requests
from PIL import Image
from io import BytesIO


add=input("широта ")
addr=input("долгота ")
address_ll = "{0},{1}".format(add, addr)
delta = "0.005"#размеры

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "sat"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)
# Read the image from the response content
image = Image.open(BytesIO(response.content))

# Show the image
image.show()
image.save("map_image.png")

