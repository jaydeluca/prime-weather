from flask_restx import Namespace, Resource

api = Namespace("Prime", description="Prime Number Service")

@api.route("/")
class PrimeResource(Resource):
    """Prime Number"""

    def get(self) -> int:
        return 3
