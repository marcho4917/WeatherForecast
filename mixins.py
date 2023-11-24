import requests
from . import API_KEY


class ConnectionMixin:
    def __init__(self):
        self.url = 'http://api.weatherapi.com/v1'
        self.api_key = API_KEY

    def connect_with_api(self, city):
        url = self.url + '/current.json?' + f'key={self.api_key}' + '&' + f'q={city}'
        response = requests.get(url)
        return response

    def load_data_from_api_to_dict(self, city):
        data = self.connect_with_api(city).json()
        weather_data = {
            "temp": data.get('temp_c'),
            "humidity": data.get('humidity'),
            "cloud": data.get('cloud'),
            "wind": data.get('wind_kph'),
            "pressure": data.get('pressure_mb'),
            "snow": data.get('daily_chance_of_snow'),
            "rain": data.get('daily_chance_of_rain')
        }
        return weather_data
