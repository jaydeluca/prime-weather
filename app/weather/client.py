import requests


class WeatherClient:
    """Client for calling the Weather API"""
    api_key = ""
    base_url = "http://api.openweathermap.org/data/2.5/"
    endpoint = "weather?zip="

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, zipcode):
        """
        https://openweathermap.org/current#zip
        :param zipcode:
        :return:
        """
        request = requests.get(self.get_path(zipcode))
        return request.json()

    def get_path(self, zipcode):
        return self.base_url + self.endpoint + zipcode + ",us&appid="+self.api_key
