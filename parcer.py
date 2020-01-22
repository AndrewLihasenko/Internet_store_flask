from flask_restful import reqparse

stores_parser = reqparse.RequestParser()
stores_parser.add_argument('title')

products_parser = reqparse.RequestParser()
products_parser.add_argument('name')
products_parser.add_argument('category')
products_parser.add_argument('store')
products_parser.add_argument('min_price')
products_parser.add_argument('max_price')

users_parser = reqparse.RequestParser()
users_parser.add_argument('name')
