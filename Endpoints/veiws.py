import requests
import datetime

import json
import os
import urllib.request as urlb

# api key is 459a67bef104c5a557e66c0fb1ea11bf

apiKey = "459a67bef104c5a557e66c0fb1ea11bf"
lat = "54.4609N"
lon = "3.0886W"
URL = "https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude={part}&appid="+apiKey
print(URL)

response = requests.get(URL)
print(response.status_code)
print(response.json())

response_url = urlb.urlopen('https://api.publicapis.org/entries')
print(response_url)


# request data from API
def get_weather_data(request):
    request.get('https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID='+apiKey)

# send data to file

# delete file

# retreive data from file

# turn data into visual rep
