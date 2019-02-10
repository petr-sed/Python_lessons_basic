
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
import time

def finder(big_string, string_part, splitter):
    first_ind = big_string.find(string_part)
    last_ind = big_string.find(splitter, first_ind)
    return big_string[first_ind + len(string_part): last_ind]

class Country:
    name = ''
    file_name = "city.list.json"
    sty_lst = []
    def get_counrtyname(self):
        self.name = input("Input country name:")
        return self.name

    def country_list(self):
        country_lst = []
        with open(self.file_name, "r", encoding='utf-8') as read_file:
            for line in read_file:
                if '"country"' in line and line[16:-3] not in country_lst and line[16:-3] is not '':
                    country_lst.append(line[16:-3])
        country_lst.sort()
        return country_lst

    def sity_list(self):
        with open("city.list.json", "r", encoding='utf-8') as read_file:
            line_prev = ''
            for line in read_file:
                if self.name in line and line_prev[13: -3] is not '' and line_prev[13: -3] is not '-':
                    self.sty_lst.append(line_prev[13: -3])
                line_prev = line
        self.sty_lst.sort()
        return self.sty_lst

class Sity:
    name = []
    file_name = "city.list.json"
    sity_id = 0

    def get_sityname(self):
        for word in input().split():
            self.name.append(word.rstrip(','))
        return self.name

    def find_id(self, sity_name):
        with open(self.file_name, "r", encoding='utf-8') as read_sity:
            line_prew = ''
            for line in read_sity:
                if '"{}"'.format(sity_name) in line:
                    self.sity_id = (line_prew[10:-2])
                line_prew = line
        if self.sity_id == 0:
            print("No sity")
            exit(0)
        return self.sity_id

class Forecast:
    api_id = ''
    weather = ''
    date = ''
    temp = ''
    weather_id = ''

    def __init__(self, sity_id):
        self.sity_id = sity_id

    def get_apiid(self):
        with open("app.id", "r", encoding='utf-8') as read_file:
            for line in read_file:
                if line.startswith('=') is not True and line != '':
                    self.api_id = line


    def get_weather(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'.format(self.sity_id, self.api_id)
        html = urllib.request.urlopen(url)
        weather = str(html.read())
        self.weather = (weather[2:-2])
        return self.weather

    def split_weather(self):
        Forecast.get_apiid(self)
        Forecast.get_weather(self)
        self.date =finder(self.weather, '"dt":', ',')
        #self.date = time.ctime(int(date))
        self.temp = finder(self.weather, '"temp":', ",")
        self.weather_id = finder(self.weather, '"weather":[{"id":', ",")
        return self.date, self.temp, self.weather_id

class DBase:
    #file_name = "weather.txt"
    #table_name = "weather_in_sity"


    def __init__(self, file_name, table_name):
        self.file_name = file_name
        self.table_name = table_name

    def make_db(self, sity_id, sity_name, country, date, temp, weather_id):
        conn_wr = sqlite3.connect(self.file_name)
        cursor_wr = conn_wr.cursor()
        cursor_wr.execute('CREATE TABLE IF NOT EXISTS {} (sity_id  PRIMARY KEY, sity_name VARCHAR,'
                          'country VARCHAR, dt VARCHAR, temp INTEGER, weather_id VARCHAR)'.format(self.table_name))
        try:
            cursor_wr.execute('INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?)'.format(self.table_name),
                           (sity_id, sity_name, country, date, temp, weather_id))
        except sqlite3.IntegrityError:
            cursor_wr.execute('UPDATE {} SET dt =?, temp =?, weather_id =?' 
                           'WHERE sity_id =?'.format(self.table_name),(date,
                                                      temp, weather_id, sity_id))
        conn_wr.commit()
        cursor_wr.close()

    def read_db(self):
        conn_r = sqlite3.connect(self.file_name)
        cursor_r = conn_r.cursor()
        for row in cursor_r.execute('SELECT rowid, * FROM {} ORDER BY sity_id'.format(self.table_name)):
            print(row)
        conn_r.commit()
        cursor_r.close()


country1 = Country()
new_base = DBase("weatherAD.txt", "weather_in_sity")
sity1 = Sity()
print(country1.country_list())
country1.get_counrtyname()
print(country1.sity_list())
for sity in sity1.get_sityname():
    ind = sity1.name.index(sity)
    forecast1 = Forecast(sity1.find_id(sity))
    forecast1.split_weather()
    new_base.make_db(sity1.sity_id, sity1.name[ind], country1.name, forecast1.date, forecast1.temp, forecast1.weather_id)

new_base.read_db()


