from flask import Blueprint
from flask_restful import Api

from users.resource import CreateUser, Basket

users_bp = Blueprint("users", __name__)
api = Api(users_bp)

api.add_resource(CreateUser, '/users', '/users/<int:user_id>')
api.add_resource(Basket, '/basket')
