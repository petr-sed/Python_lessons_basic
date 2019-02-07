
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import urllib.request


def find_id(sity_name):
    with open("city.list.json", "r", encoding='utf-8') as read_sity:
        line_prew = ''
        sity_id = ''
        for line in read_sity:
            if '"{}"'.format(sity_name) in line:
                sity_id = line_prew[10:-2]
            line_prew = line
    if sity_id is '':
       sity_id = "No sity"
    return sity_id


def get_weather(sity_id):
    html =  urllib.request.urlopen('http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1')
    f = html.read()
    print(f)



