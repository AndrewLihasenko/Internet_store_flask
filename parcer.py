from flask_restful import reqparse

stores_parser = reqparse.RequestParser()
stores_parser.add_argument('name')

