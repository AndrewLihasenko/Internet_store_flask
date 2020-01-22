from flask import json, request
from flask_restful import Resource, marshal_with

from db import db
from marshal_structure import users_structure
from model import Users
from parcer import users_parser


class CreateUser(Resource):
    @marshal_with(users_structure)
    def get(self):
        user_name = users_parser.parse_args().get('name')
        if user_name:
            user = Users.query.filter(Users.name.match(user_name)).first()
            return user, 200
        return Users.query.all(), 200

    @marshal_with(users_structure)
    def post(self):
        ...

    @marshal_with(users_structure)
    def patch(self):
        ...

    def delete(self):
        ...
