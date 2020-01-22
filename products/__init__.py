from flask import Blueprint
from flask_restful import Api

from products.resource import CreateProducts

products_bp = Blueprint("products", __name__)
api = Api(products_bp)

api.add_resource(CreateProducts, '/products', '/products/<int:product_id>')
