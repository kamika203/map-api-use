import requests
from PIL import Image
from io import BytesIO

stadiums_location = {"Лужники": "37.554191,55.715551",
                     "Спартак": "37.440262,55.818015",
                     "Динамо": "37.559809,55.791540"
                     }

delta = "0.2"#размеры

map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": stadiums_location['Лужники'],
    "spn": ",".join([delta, delta]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": "{0},pm2rdm~{1},pm2dgl~{2},pm2bll".format(stadiums_location['Лужники'],stadiums_location['Спартак'],stadiums_location['Динамо'])
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)


# Read the image from the response content
image = Image.open(BytesIO(response.content))

# Show the image
image.show()
