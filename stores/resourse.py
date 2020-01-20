from flask import json, request
from flask_restful import Resource, marshal_with

from db import db
from marshal_structure import stores_structure
from model import Stores
from parcer import stores_parser


class CreateStore(Resource):
    @marshal_with(stores_structure)
    def get(self):
        store_name = stores_parser.parse_args().get('name')
        if store_name:
            store = Stores.query.filter_by(name=store_name).first()
            return store, 200
        return Stores.query.all(), 200

    def post(self):
        data = json.loads(request.data)
        if Stores.query.filter(Stores.name == data.get('name')).first():
            return "This store name are exist", 400
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
