from flask import request
from flask_accepts import accepts
from flask_restx import Namespace, Resource

from .schema import WeatherSchema
from .service import WeatherService

api = Namespace("Weather", description="Weather Service")


@api.route("/weather")
class PrimeResource(Resource):

    @accepts(schema=WeatherSchema, api=api)
    def post(self):
        """Returns the Weather of the provided zipcode"""
        number = request.get_json()["zipcode"]

        return WeatherService.get_weather(number)
