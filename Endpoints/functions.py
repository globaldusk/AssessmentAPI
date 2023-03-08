# api key is 459a67bef104c5a557e66c0fb1ea11bf

apiKey = "459a67bef104c5a557e66c0fb1ea11bf"

# read data from file
def read_data_from_file(file):
    with open(file, 'r') as f:
        return f.read().split('/')


#get weather Json from API link
def get_weather_data(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat=' + lat + '&lon=' + lon + '&appid=' + apiKey
    url = url.strip()
    print(url)

    return url



# send data to file
def write_weather_to_file(linesToWrite, file):
    with open(file, 'w') as f:
        f.writelines(linesToWrite)