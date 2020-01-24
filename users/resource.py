from flask import json, request
from flask_restful import Resource, marshal_with

from db import db
from marshal_structure import users_structure, products_structure
from model import Users, Products
from parcer import users_parser


class CreateUser(Resource):
    @marshal_with(users_structure)
    def get(self):
        user_name = users_parser.parse_args().get('name')
        if user_name:
            user = Users.query.filter_by(name=user_name).first() or \
                   Users.query.filter(Users.name.match(user_name)).all()
            return user, 200
        return Users.query.all(), 200

    @marshal_with(users_structure)
    def post(self):
        data = json.loads(request.data)
        if Users.query.filter(Users.name == data.get('name')).first():
            return "This user name are exist", 400
        user = Users(**data)
        try:
            db.session.add(user)
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return user, 201

    def delete(self, user_id):
        user = Users.query.get(user_id)
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
            except (ConnectionError, PermissionError) as err:
                return err, 400
            return "User was deleted", 200
        return "Sorry. Nothing change.", 400


class Basket(Resource):
    def post(self):
        data = json.loads(request.data)
        user_name = data.get('user_name')
        product_name = data.get('product_name')
        user = Users.query.filter_by(name=user_name).first()
        product = Products.query.filter_by(name=product_name).first()
        if user and product:
            user.basket.append(product)
        else:
            return "Invalid data entered"
        try:
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return f"{user.name} added {product.name} to basket"

    @marshal_with(products_structure)
    def get(self):
        args = users_parser.parse_args(strict=True)
        user = Users.query.filter_by(name=args.get('name')).first()
        return user.basket, 200
