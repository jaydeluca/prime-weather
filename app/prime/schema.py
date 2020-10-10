from marshmallow import fields, Schema


class PrimeSchema(Schema):
    """Prime Service Schema"""
    number = fields.Number(attribute="number")
