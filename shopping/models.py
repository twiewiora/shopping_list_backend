from sqlalchemy.orm import relationship

from shopping.main import db


class ShoppingItem(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    amount = db.Column(db.Integer())
    bought = db.Column(db.Boolean())

    def __init__(self, name, amount, bought):
        self.name = name
        self.amount = amount
        self.bought = bought

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'amount': self.amount,
            'bought': self.bought
        }


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    products = relationship('Product', backref='category')
    product_list = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'products': self.product_list
        }


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))

    def __init__(self, name, category):
        self.name = name
        self.category_id = category.id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'categoryId': self.category_id
        }
