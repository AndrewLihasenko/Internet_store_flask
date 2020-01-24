from flask import json, request
from flask_restful import Resource, marshal_with
from sqlalchemy.orm.exc import FlushError

from db import db
from marshal_structure import stores_structure, products_structure
from model import Stores, Products
from parcer import stores_parser


class CreateStore(Resource):
    @marshal_with(stores_structure)
    def get(self):
        store_name = stores_parser.parse_args().get('title')
        if store_name:
            store = Stores.query.filter_by(title=store_name).first()
            return store, 200
        return Stores.query.all(), 200

    @marshal_with(stores_structure)
    def post(self):
        data = json.loads(request.data)
        if Stores.query.filter(Stores.title == data.get('title')).first():
            return "This store title are exist", 400
        store = Stores(**data)
        try:
            db.session.add(store)
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return store, 201

    @marshal_with(stores_structure)
    def patch(self, store_id):
        data = json.loads(request.data)
        store = Stores.query.get(store_id)
        if store:
            store.owner = data.get('owner')
            try:
                db.session.commit()
            except (ConnectionError, PermissionError) as err:
                return err, 400
            return store, 201
        return "Sorry. Nothing change.", 400

    def delete(self, store_id):
        store = Stores.query.get(store_id)
        if store:
            try:
                db.session.delete(store)
                db.session.commit()
            except (ConnectionError, PermissionError) as err:
                return err, 400
            return "Store was deleted", 200
        return "Sorry. Nothing change.", 400


class StoresProducts(Resource):
    def post(self):
        data = json.loads(request.data)
        store_title = data.get('store_title')
        product_name = data.get('product_name')
        store = Stores.query.filter_by(title=store_title).first()
        product = Products.query.filter_by(name=product_name).first()
        if store and product:
            store.products.append(product)
        else:
            return "Invalid data entered"
        try:
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return f"{product.name} added to {store.title}"

    @marshal_with(products_structure)
    def get(self):
        args = stores_parser.parse_args(strict=True)
        store = Stores.query.filter_by(title=args.get('title')).first()
        return store.products, 200

    def delete(self):
        data = json.loads(request.data)
        store_title = data.get('store_title')
        product_name = data.get('product_name')
        store = Stores.query.filter_by(title=store_title).first()
        product = Products.query.filter_by(name=product_name).first()
        if store and product:
            store.products.remove(product)
        else:
            return "Invalid data entered"
        try:
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return f"{product.name} was deleted from {store.title}"
