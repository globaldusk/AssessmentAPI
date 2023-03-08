import requests

from functions import *

# api key is 459a67bef104c5a557e66c0fb1ea11bf

apiKey = "459a67bef104c5a557e66c0fb1ea11bf"

linesToWrite = []


lines = read_data_from_file("locations.txt")

for line in lines:
    # breaks the coordinates into lat and lon
    line = line.split(',')
    lat = line[0]
    lon = line[1]

    # less typing by using .session()
    with requests.session() as s:
        # uses method from functions file
        s.get(get_weather_data(lat, lon))

        # the raw Json
        data = s.get(get_weather_data(lat, lon)).json()

        # printing to test the output
        print(data)
        name = data['city']['name']
        data = data['list'][0]

        # printing to test the output
        print(data)
        currentCondition = data['weather'][0]['main']
        temp = data['main']['temp']

        # writing all the data to user-friendly format
        weatherString = (name + ": the weather is " + currentCondition + " and the temp is " + str(temp) + "\n")
        linesToWrite.append(weatherString)
        write_weather_to_file(linesToWrite, 'weather.txt')
