from flask import Blueprint
from flask_restful import Api

from stores.resource import CreateStore

stores_bp = Blueprint("stores", __name__)
api = Api(stores_bp)

api.add_resource(CreateStore, '/stores', '/stores/<int:store_id>')
