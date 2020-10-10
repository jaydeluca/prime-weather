from marshmallow import fields, Schema


class WeatherSchema(Schema):
    """Weather Service Schema"""
    zipcode = fields.String(attribute="zipcode")
