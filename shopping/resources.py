from flask_restful import Resource

from shopping.main import db, parser
from shopping.models import ShoppingItem


class Item(Resource):
    @staticmethod
    def delete(item_id):
        try:
            item = ShoppingItem.query.filter_by(id=int(item_id)).first()
            db.session.delete(item)
            db.session.commit()
            return {'result': 'deleted'}, 204
        except Exception as e:
            return str(e)


class ItemList(Resource):
    @staticmethod
    def get():
        try:
            items = ShoppingItem.query.all()
            items.sort(key=lambda item: (item.bought, item.id))
            return [item.serialize() for item in items]
        except Exception as e:
            return str(e)


class ItemCreate(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        try:
            item = ShoppingItem(
                name=args['name'],
                amount=1,
                bought=False
            )
            db.session.add(item)
            db.session.commit()
            return item.serialize(), 201
        except Exception as e:
            return str(e)


class ItemChangeAmount(Resource):
    @staticmethod
    def put(item_id):
        args = parser.parse_args()
        try:
            item = ShoppingItem.query.filter_by(id=int(item_id)).first()
            item.amount = int(args['amount'])
            db.session.commit()
            return item.serialize(), 201
        except Exception as e:
            return str(e)


class ItemChangeBuyStatus(Resource):
    @staticmethod
    def put(item_id):
        try:
            item = ShoppingItem.query.filter_by(id=int(item_id)).first()
            item.bought = not item.bought
            db.session.commit()
            return item.serialize(), 201
        except Exception as e:
            return str(e)
