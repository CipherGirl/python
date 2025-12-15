import requests

def get_weather(city):
    response = requests.get(f'http://api.weatherapi.com/v1/{city}')
    if response.status_code == 200:
        return response.json()
       
    else:
        raise ValueError("Could not retrieve weather data")