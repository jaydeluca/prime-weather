import requests
from flask import current_app


class WeatherClient:
    """Client for calling the Weather API"""
    api_key = ""
    base_url = "http://api.openweathermap.org/data/2.5/"
    endpoint = "weather?zip="

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, zipcode):
        """
        Get Weather
        @TODO: add caching (15 minute ttl?) by #zipcode to avoid excess external calls
        https://openweathermap.org/current#zip
        :param zipcode:
        :return: json of current weather
        """
        request = requests.get(self.get_path(zipcode))
        current_app.logger.info("Call to external api response code: " + str(request.status_code))
        return request.json()

    def get_path(self, zipcode):
        return self.base_url + self.endpoint + zipcode + ",us&appid="+self.api_key
