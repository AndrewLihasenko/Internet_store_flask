from flask import Blueprint
from flask_restful import Api

from stores.resource import CreateStore, StoresProducts

stores_bp = Blueprint("stores", __name__)
api = Api(stores_bp)

api.add_resource(CreateStore, '/stores', '/stores/<int:store_id>')
api.add_resource(StoresProducts, '/stores_products')

