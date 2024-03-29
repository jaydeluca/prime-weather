from flask import request
from flask_accepts import accepts
from flask_restx import Namespace, Resource
import json
from random import randint
from time import sleep

from .schema import PrimeSchema
from .service import PrimeService

api = Namespace("Prime", description="Prime Number Service")


@api.route("/is_prime")
class PrimeResource(Resource):

    @accepts(schema=PrimeSchema, api=api)
    def post(self):
        """Checks if a number is prime"""
        number = request.get_json()["number"]

        sleep(randint(1, 10))

        return json.dumps(PrimeService.is_prime(number))
