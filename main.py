import requests
import json

from datetime import datetime



def getting_current_time():
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    return str(current_date)[:10]

def getting_weather():
    api = 'c8ef805da30352a66abc2f32d70340f9'
    city = 'Kyiv' 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"

    response = requests.get(url=url)
    weather_date = response.json()

    collecting_info(weather_date)
    
def collecting_info(data):

    converting_temperature = lambda number : round((number - 273.15), 1)
    
    temperature = converting_temperature(round((int(data['main']['temp'])), 1))
    temperature_min = converting_temperature(round((int(data['main']['temp_min'])), 1))
    temperature_max = converting_temperature(round((int(data['main']['temp_max'])), 1))
    
    type_of_weather = data['weather'][0]['main']
    wind_speed = data['wind']['speed']
    city = data['name']
    list = {'city': city,
            "temperature" : temperature,
            "temperature_min" : temperature_min,
            "temperature_max" : temperature_max,
            "type_of_weather" : type_of_weather,
            "wind_speed" : wind_speed
            }
    
    formatted_date = getting_current_time()
    with open (f'weather_data_for_{formatted_date}.json', 'w') as json_file:
        json.dump(list, json_file, indent=4,ensure_ascii=False)






def main():
    getting_weather()



if __name__ == '__main__':
    main()





