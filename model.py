from db import db

ADMIN_ROLE = 0
BUYER_ROLE = 1


class Users(db.Model):
    __tablename__ = "users_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=BUYER_ROLE)


class Stores(db.Model):
    __tablename__ = "stores_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(120), index=True)
    title = db.Column(db.String(120), index=True, unique=True)
    owner = db.Column(db.String(120), index=True)


class Products(db.Model):
    __tablename__ = "products_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    price = db.Column(db.Integer, index=True, nullable=False)
    category = db.Column(db.String(120), index=True)
    # store = db.Column(db.String(120))
    description = db.Column(db.String())
    # image =
