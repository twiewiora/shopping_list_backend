import os

from flask import Flask
from flask_restful import Api, reqparse, Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from shopping.models import ShoppingItem

app = Flask(__name__)
api = Api(app)

app.config.from_object("shopping.config." + os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('amount')


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
            items.sort(key=lambda item: item.bought, reverse=True)
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


api.add_resource(ItemList, '/items')
api.add_resource(ItemCreate, '/item')
api.add_resource(Item, '/item/<item_id>')
api.add_resource(ItemChangeAmount, '/item/<item_id>/changeAmount')
api.add_resource(ItemChangeBuyStatus, '/item/<item_id>/changeBuyStatus')
