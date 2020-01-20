from flask_restful import fields

stores_structure = {
    "id": fields.Integer,
    "city": fields.String,
    "name": fields.String,
    "owner": fields.String
}

