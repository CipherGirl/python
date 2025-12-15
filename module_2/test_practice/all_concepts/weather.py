import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}')
        
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json()

        return data['current']['temp_c']


