from flask import json, request
from flask_restful import Resource, marshal_with

from db import db
from marshal_structure import products_structure
from model import Products
from parcer import products_parser


class CreateProducts(Resource):
    @marshal_with(products_structure)
    def get(self):
        product_name = products_parser.parse_args().get('name')
        category_name = products_parser.parse_args().get('category')
        store_name = products_parser.parse_args().get('store')
        min_price = products_parser.parse_args().get('min_price')
        max_price = products_parser.parse_args().get('max_price')
        if product_name:
            product = Products.query.filter_by(name=product_name).first() or \
                      Products.query.filter(Products.name.match(product_name)).all()
            return product, 200
        if category_name:
            product = Products.query.filter_by(category=category_name).all() or \
                      Products.query.filter(Products.category.match(category_name)).all()
            return product, 200
        if store_name:
            product = Products.query.filter_by(name=store_name).first()
            return product, 200
        if min_price:
            product = Products.query.filter(Products.price >= min_price,
                                            Products.price <= max_price).all()
            return product, 200
        return Products.query.all(), 200

    @marshal_with(products_structure)
    def post(self):
        data = json.loads(request.data)
        if Products.query.filter(Products.name == data.get('name')).first():
            return "This product name are exist", 400
        product = Products(**data)
        try:
            db.session.add(product)
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return product, 201

    @marshal_with(products_structure)
    def patch(self, product_id):
        data = json.loads(request.data)
        product = Products.query.get(product_id)
        if product:
            product.description = data.get('description')
            try:
                db.session.commit()
            except (ConnectionError, PermissionError) as err:
                return err, 400
            return product, 201
        return "Sorry. Nothing change.", 400

    def delete(self, product_id):
        product = Products.query.get(product_id)
        if product:
            try:
                db.session.delete(product)
                db.session.commit()
            except (ConnectionError, PermissionError) as err:
                return err, 400
            return "Product was deleted", 200
        return "Sorry. Nothing change.", 400
