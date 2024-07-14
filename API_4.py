import requests


city_list = input("Введите список городов через запятую: ").split(",")

# Инициализируем переменные
southern_latitude = float('inf')
southern_city = ""
max_s_l=90
s_city=""
search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
search_params = {
        "apikey": api_key,
        "text": '',
        "lang": "ru_RU",
        "type": "geo"
    }

# Перебираем список городов и запрашиваем данные о координатах каждого города
for city in city_list:
    city = city.strip()  # Удаляем возможные пробелы в начале и конце названия города
    if city == "":
        continue
    try:
        search_params["text"]=city
        response = requests.get(search_api_server, params=search_params)
        json_response = response.json()
        point=json_response['features'][0]['geometry']['coordinates']
        lat=float(point[1])
        if (lat<max_s_l):
            max_s_l=lat
            s_city=city
    except:
        print(f"Не удалось найти координаты для города {city}.")
        continue
if s_city != "":
    print(f"Самый южный город: {s_city}")
else:
    print("Не введено ни одного города.")
