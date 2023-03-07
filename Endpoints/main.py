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
    lon = line[1]

    with requests.session() as s:
        s.get(get_name_data(lat, lon))

        data = s.get(get_name_data(lat, lon)).json()


    print(data)
    if (data != []):
        jsonDict = data[0]
        print(jsonDict)

        country = jsonDict['country']
        state = jsonDict['state']
        #weatherJson = .json()


    else:
        print("No weather data available at these coordinates")
