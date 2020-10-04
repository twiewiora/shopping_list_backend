from main import db


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
