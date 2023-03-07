from functions import *

# api key is 459a67bef104c5a557e66c0fb1ea11bf

apiKey = "459a67bef104c5a557e66c0fb1ea11bf"
lat = ""
long = ""
country = ""
state = ""

weatherJson = ""

lines = read_data_from_file("locations.txt")

for line in lines:

    line = line.split(',')

    lat = line[0]
    print(lat)
    lon = line[1]
    print(lon)

    weatherJson = get_name_data(lat, lon).json()
    print(weatherJson)
