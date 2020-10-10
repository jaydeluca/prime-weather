from flask import current_app
from .client import WeatherClient


class WeatherService:

    @staticmethod
    def get_weather(zipcode):
        """Uses Weather API Client to return Current Weather"""
        api_key = current_app.config["API_KEY"]
        weather_client = WeatherClient(api_key)

        return weather_client.get_weather(zipcode)
