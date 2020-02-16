from flask import Blueprint
from flask_restful import Api

from users.resource import CreateUser, Order, GetMoney

users_bp = Blueprint("users", __name__)
api = Api(users_bp)

api.add_resource(CreateUser, '/users', '/users/<int:user_id>')
api.add_resource(Order, '/order', '/order/<int:order_id>')
api.add_resource(GetMoney, '/user_money', '/user_money/<int:user_id>')
