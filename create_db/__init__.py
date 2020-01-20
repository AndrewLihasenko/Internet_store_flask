from flask import Blueprint
from flask_restful import Api

from create_db.db_model import CreateDB

create_db = Blueprint("create_db", __name__)
api = Api(create_db)

api.add_resource(CreateDB, "/create_db")
