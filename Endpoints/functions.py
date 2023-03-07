import requests
import datetime

import json
import os
import urllib.request as urlb

# api key is 459a67bef104c5a557e66c0fb1ea11bf

apiKey = "459a67bef104c5a557e66c0fb1ea11bf"
# lat = "54.4609"
# lon = "3.0886"
country = "GB"
state = "england"
# coordURL = "https://api.openweathermap.org/geo/1.0/reverse?lat=" + lat + "&lon=" + lon + "&limit=5&appid=" + apiKey
# nameURL = "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&exclude=hourly,
# daily&appid=" + apiKey

# print(coordURL)

data = ""
lines = ""

# response = requests.get(coordURL)
# print(response.status_code)
# print(response.json())

# response_url = urlb.urlopen('https://api.publicapis.org/entries')
# print(response_url)
# a = (requests.get("https://api.openweathermap.org/geo/1.0/reverse?lat=54.4609&lon=-3.0886&limit=5&appid"
#                  "=459a67bef104c5a557e66c0fb1ea11bf"))
# print(a.json())


# read data from file
def read_data_from_file(file):
    with open(file, 'r') as f:
        return f.read().split('/')


def get_name_data(lat, lon):
    url = 'https://api.openweathermap.org/geo/1.0/reverse?lat=' + lat + '&lon=' + lon + '&limit=5&appid=' + apiKey
    url = url.strip()
    print(url)

    return url


# request data from API
def get_weather_data(coordURL):
    response = requests.get(coordURL)
    response.json()
    # sort from json to data
    # return data


# send data to file
def write_weather_to_file(request):
    request.get('https://api.openweathermap.org/data/2.5/weatssssher?q=London,uk&APPID=' + apiKey)
# delete file

# retreive data from file

# turn data into visual rep
