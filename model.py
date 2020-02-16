from db import db

ADMIN_ROLE = 0
BUYER_ROLE = 1


stores_products = db.Table(
    'stores_products',
    db.Column('store_id', db.Integer, db.ForeignKey('stores_table.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products_table.id'))
)


class OrderProduct(db.Model):
    __tablename__ = 'order_product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products_table.id'), primary_key=True)
    is_paid = db.Column(db.Boolean, default=False)
    money = db.Column(db.Integer, default=0)

    user = db.relationship('User', backref=db.backref('order_products'), cascade='all')
    product = db.relationship('Product', backref=db.backref('order_products'), cascade='all')


class User(db.Model):
    __tablename__ = "users_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=BUYER_ROLE)
    products = db.relationship('Product', secondary='order_product')


class Store(db.Model):
    __tablename__ = "stores_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(120), index=True)
    title = db.Column(db.String(120), index=True, unique=True)
    owner = db.Column(db.String(120), index=True)
    products = db.relationship('Product', secondary=stores_products, backref=db.backref('products_ref'))


class Product(db.Model):
    __tablename__ = "products_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    price = db.Column(db.Integer, index=True, nullable=False)
    category = db.Column(db.String(120), index=True)
    description = db.Column(db.String())
    # image =
    users = db.relationship('User', secondary='order_product')
