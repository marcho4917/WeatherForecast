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

    def connect_with_api_forecast(self, city):
        url = self.url + '/forecast.json?' + f'key={self.api_key}' + '&' + f'q={city}'
        response = requests.get(url)
        return response

    def load_data_from_api_to_dict(self, city):
        data = self.connect_with_api(city).json()
        forecast_data = self.connect_with_api_forecast(city).json()
        print(data)
        print(forecast_data)
        weather_data = {
            "name": data['location']['name'],
            "temp": data['current']['temp_c'],
            "humidity": data['current']['humidity'],
            "cloud": data['current']['cloud'],
            "wind": data['current']['wind_kph'],
            "pressure": data['current']['pressure_mb'],
            "rain": forecast_data['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
            "snow": forecast_data['forecast']['forecastday'][0]['day']['daily_chance_of_snow'],
        }
        return weather_data
