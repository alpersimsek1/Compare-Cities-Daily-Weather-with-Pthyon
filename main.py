from weather import City
from backend import Database
import requests
import json

d = Database("cities.db")
api_key = "0a2d6b9962bbd0ed42dc2eef8cea7124"

def create_city(cityid):
    r = requests.get('http://api.openweathermap.org/data/2.5/group?id='+ str(cityid) +'&units=metric&appid='+api_key+'')
    data = json.loads(r.text)
    field_list = data['list']
    c = City()
    for i in field_list:
        c.city_name = i['name']
        c.temperature = i['main']['temp']
        c.temp_max = i['main']['temp_max']
        c.temp_min = i['main']['temp_min']

    c.city_id = cityid
    d.insert(c.city_name,c.datenow,c.temperature,c.temp_min,c.temp_max)
    return c

amsterdam = create_city(5107152)
losAngeles = create_city(3882428)
boston = create_city(4930956)
zurich = create_city(2657896)
cities = [amsterdam,losAngeles,boston,zurich]

for city in cities:
    print(city.__str__())
