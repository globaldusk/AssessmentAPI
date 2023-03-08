from functions import *

# api key is 459a67bef104c5a557e66c0fb1ea11bf

apiKey = "459a67bef104c5a557e66c0fb1ea11bf"
lat = ""
long = ""
name = ""
currentCondition = ""
temp = ""
linesToWrite = []

weatherJson = ""

lines = read_data_from_file("locations.txt")

for line in lines:

    line = line.split(',')

    lat = line[0]
    lon = line[1]

    with requests.session() as s:
        s.get(get_weather_data(lat, lon))

        data = s.get(get_weather_data(lat, lon)).json()

        print(data)
        name = data['city']['name']
        data = data['list'][0]
        print(data)
        currentCondition = data['weather'][0]['main']
        temp = data['main']['temp']
        weatherString = (name+": the weather is "+currentCondition+" and the temp is "+str(temp)+"\n")
        linesToWrite.append(weatherString)
        write_weather_to_file(linesToWrite, 'weather.txt')
