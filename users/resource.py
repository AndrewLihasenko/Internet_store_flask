from flask import json, request
from flask_restful import Resource, marshal_with

from db import db
from marshal_structure import users_structure, products_structure
from model import User, Product, OrderProduct
from parcer import users_parser


class CreateUser(Resource):
    @marshal_with(users_structure)
    def get(self):
        user_name = users_parser.parse_args().get('name')
        if user_name:
            user = User.query.filter_by(name=user_name).first() or \
                   User.query.filter(User.name.match(user_name)).all()
            return user, 200
        return User.query.all(), 200

    @marshal_with(users_structure)
    def post(self):
        data = json.loads(request.data)
        if User.query.filter(User.name == data.get('name')).first():
            return "This user name are exist", 400
        user = User(**data)
        try:
            db.session.add(user)
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return user, 201

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
            except (ConnectionError, PermissionError) as err:
                return err, 400
            return "User was deleted", 200
        return "Sorry. Nothing change.", 400


class Order(Resource):
    def post(self):
        data = json.loads(request.data)
        user_name = data.get('user_name')
        product_name = data.get('product_name')
        user = User.query.filter_by(name=user_name).first()
        product = Product.query.filter_by(name=product_name).first()
        if user and product:
            user.products.append(product)
        else:
            return "Invalid data entered", 400
        try:
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return f"{user.name} added {product.name} to basket", 201

    @marshal_with(products_structure)
    def get(self):
        args = users_parser.parse_args(strict=True)
        user = User.query.filter_by(name=args.get('name')).first()
        paid_status = users_parser.parse_args().get('is_paid')
        if paid_status:
            order_products = OrderProduct.query.filter_by(is_paid=paid_status).all()
            return [is_paid_prod.product for is_paid_prod in order_products], 200
        return user.products, 200

    def patch(self, order_id):
        data = json.loads(request.data)
        order_products = OrderProduct.query.filter_by(is_paid='False').all()
        for prod in order_products:
            if prod.product.id == order_id:
                prod.is_paid = data.get('is_paid')
                prod.money = prod.money - prod.product.price
                try:
                    db.session.commit()
                except (ConnectionError, PermissionError) as err:
                    return err, 400
                return f"{prod.product.name} was paid", 201
            return "Payment failed", 400


class GetMoney(Resource):
    def patch(self, user_id):
        data = json.loads(request.data)
        order_products = OrderProduct.query.all()
        for prod in order_products:
            if prod.user.id == user_id:
                prod.money = data.get('add_money')
                try:
                    db.session.commit()
                except (ConnectionError, PermissionError) as err:
                    return err, 400
                return f"{prod.user.name} added {data.get('add_money')}$ to wallet", 201
            return "Operation failed", 400


    def get(self):
        args = users_parser.parse_args(strict=True)
        user = User.query.filter_by(name=args.get('name')).first()
        if user:
            order_products = OrderProduct.query.all()
            for prod in order_products:
                if prod.user.id == user.id:
                    return f"{prod.user.name} has {prod.money}$", 200
        return "This user not found", 400
