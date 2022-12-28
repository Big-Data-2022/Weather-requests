import requests
from pprint import pprint
from datetime import datetime
import os 
os.system('clear')

city  = input('City name: ')
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6cbdba99aa2fa63ef0e4b62225464e98&units=metric"
response = requests.get(url)
data = response.json()
#pprint(data)
city_description = data['weather'][0]
all_weather = ['Smoke', 'Clouds', 'Clear', 'Tornado', 'Dust', 'Sand', 
            'Fog', 'Haze', 'Mist', 'Snow', 'Rain', 'Drizzle', 'Thunderstorm']
for i in all_weather:
    if city_description['main'] == 'Smoke':
        city_description_main = f'\U0001F324 {city_description["main"]}'
        
    elif city_description['main'] == 'Clouds':
        city_description_main = f'\U0001F325 {city_description["main"]}'
        
    elif city_description['main'] == 'Clear':
        city_description_main = f'\U00002600 {city_description["main"]}'
        
    elif city_description['main'] == 'Tornado':
        city_description_main = f'\U0001F32A {city_description["main"]}'
            
    elif city_description['main'] == 'Dust':
        city_description_main = f'\U0001F300 {city_description["main"]}'
        
    elif city_description['main'] == 'Sand':
        city_description_main = f'\U0001F300 {city_description["main"]}'
        
    elif city_description['main'] == 'Fog':
        city_description_main = f'\U0001F32B {city_description["main"]}'  
        
    elif city_description['main'] == 'Haze':
        city_description_main = f'\U0001F32B {city_description["main"]}'
        
    elif city_description['main'] == 'Mist':
        city_description_main = f'\U0001F32B {city_description["main"]}'
        
    elif city_description['main'] == 'Snow':
        city_description_main = f'\U000026C4 {city_description["main"]} можно идти делать снеговика'
    
    elif city_description['main'] == 'Rain':
        city_description_main = f'\U0001F327 {city_description["main"]} не выходи из дома'
        
    elif city_description['main'] == 'Drizzle':
        city_description_main = f'\U0001F326 {city_description["main"]}'
        
    elif city_description['main'] == 'Thunderstorm':
        city_description_main = f'\U0001F329 {city_description["main"]}'
    
    else:
        city_description_main = city_description["main"]

city_name = data['name']
city_temp = data['main']['temp']
city_temp_feel_like = data['main']['feels_like']
city_humidity = data['main']['humidity']
city_pressure = data['main']['pressure']
city_sunset = datetime.fromtimestamp(data['sys']['sunset'])
city_day_lenght = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(data['sys']['sunrise'])
city_sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
city_wind = data['wind']['speed']
city_visibility = data['visibility']


information_weather = f"""
Погода в городе: {city_name}
    Описание погоды: {city_description_main}
    Температура: {city_temp} С
    Ощущается как: {city_temp_feel_like} С
    Влажность: {city_humidity} %
    Давление: {city_pressure} гПа
    Скорость ветра: {city_wind} м/с
    Восход солнца: {city_sunrise}
    Продолжительность дня: {city_day_lenght}
    Закат солнца: {city_sunset}
    Область видимости: {city_visibility} метров
"""

print(information_weather)