from flask_restful import fields

products_structure = {
    "id": fields.Integer,
    "name": fields.String,
    "price": fields.Integer,
    "category": fields.String,
    "description": fields.String
}

stores_structure = {
    "id": fields.Integer,
    "city": fields.String,
    "title": fields.String,
    "owner": fields.String,
    "products": fields.Nested(products_structure)
}

users_structure = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "role": fields.Integer
}

