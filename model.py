from db import db

ADMIN_ROLE = 0
BUYER_ROLE = 1


stores_products = db.Table(
    'stores_products',
    db.Column('store_id', db.Integer, db.ForeignKey('stores_table.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products_table.id'))
)


basket = db.Table(
    'basket',
    db.Column('user_id', db.Integer, db.ForeignKey('users_table.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products_table.id')),
)


class Users(db.Model):
    __tablename__ = "users_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=BUYER_ROLE)
    basket = db.relationship('Products', secondary=basket, backref=db.backref('basket_ref'))


class Stores(db.Model):
    __tablename__ = "stores_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(120), index=True)
    title = db.Column(db.String(120), index=True, unique=True)
    owner = db.Column(db.String(120), index=True)
    products = db.relationship('Products', secondary=stores_products, backref=db.backref('products_ref'))


class Products(db.Model):
    __tablename__ = "products_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    price = db.Column(db.Integer, index=True, nullable=False)
    category = db.Column(db.String(120), index=True)
    # store = db.Column(db.String(120))
    description = db.Column(db.String())
    # image =
