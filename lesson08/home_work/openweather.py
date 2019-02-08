
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
#import csv
import json
import urllib.request
import sqlite3

sity_id = 0
sity_name = ''
country = ''
date = ''
temp = 0
weather_id = 0
api_id = ''

def find_id(sity_nm):
    global sity_id
    with open("city.list.json", "r", encoding='utf-8') as read_sity:
        line_prew = ''
        for line in read_sity:
            if '"{}"'.format(sity_nm) in line:
                sity_id = int(line_prew[10:-2])
            line_prew = line
    if sity_id == 0:
       sity_id = "No sity"
    return sity_id

def country_list():
    country_lst = []
    with open("city.list.json", "r", encoding='utf-8') as read_file:
        for line in read_file:
            if '"country"' in line and line[16:-3] not in country_lst and line[16:-3] is not '':
                country_lst.append(line[16:-3])
    country_lst.sort()
    print(country_lst)

def sity_list(cntry_name):
    sity_lst =[]
    with open("city.list.json", "r", encoding='utf-8') as read_file:
        line_prev = ''
        for line in read_file:
            if cntry_name in line and line_prev[13: -3] is not '' and line_prev[13: -3] is not '-' :
                sity_lst.append(line_prev[13: -3])
            line_prev = line
    sity_lst.sort()
    return sity_lst

def get_apiid():
    with open("app.id", "r", encoding='utf-8') as read_file:
        for line in read_file:
            if line.startswith('=') is not True and line != ' ':
                 global api_id
                 api_id= line

def get_weather(s_id, a_id):
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'.format(s_id, a_id)
    html =  urllib.request.urlopen(url)
    sity_weather = str(html.read())
    sity_weather = sity_weather[2:-2]
    return sity_weather

def finder(big_string, string_part, spliter):
    first_ind = big_string.find(string_part)
    last_ind = big_string.find(spliter, first_ind)
    return big_string[first_ind + len(string_part): last_ind]

def split_weather(sity_weather):
    global date
    global temp
    global weather_id
    date = finder(sity_weather, '"dt":', ',')
    temp = finder(sity_weather, '"temp":', ",")
    weather_id = finder(sity_weather, '"weather":[{"id":', ",")

def make_db(s_id, s_name, cntry, d, t, w_id):
    conn = sqlite3.connect("weather")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_in_sity (sity_id  PRIMARY KEY, 
                       sity_name TEXT, country TEXT, date TEXT, temp INTEGER, weather_id TEXT)''')
    try:
        cursor.execute('''INSERT INTO weather_in_sity VALUES (?, ?, ?, ?, ?, ?)''',
                           (s_id, s_name, cntry, d, t, w_id))
    except sqlite3.IntegrityError:
        cursor.execute('''UPDATE weather_in_sity SET date =?, temp =?, weather_id =? 
                           WHERE sity_id =? ''', (d, t, w_id, s_id))
    conn.commit()
    conn.commit()
    cursor.close()


get_apiid()
find_id("Sochi")
weather_j = get_weather(sity_id, api_id)
split_weather(weather_j)
print(sity_id)
print(sity_name)
print(date)
print(temp)
print(weather_id)
print(api_id)