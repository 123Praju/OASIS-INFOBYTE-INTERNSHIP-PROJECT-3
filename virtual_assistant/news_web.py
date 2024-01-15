import requests
from sk import *

api_addres = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-11&sortBy=publishedAt&apiKey="+key
json_data = requests.get(api_addres).json()

nws = []

def news():
    for i in range (5):
        nws.append(str(i+1) + " , " + json_data["articles"][i]["title"] + ".")
    return nws


