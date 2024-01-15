import requests
from sk import *

city = 'Delhi'
country_code = 'IN'

api_address = (f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID=")+key2
json_data=requests.get(api_address).json()

def temp():
    temprature=round(json_data['main']['temp']-273,1)
    return temprature

def des():
    description = json_data['weather'][0]['description']
    return description

